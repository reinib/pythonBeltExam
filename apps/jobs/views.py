from django.shortcuts import render, redirect
from .models import Job
from ..login_app.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    me = User.objects.get(id = request.session['user_id'])
    context = {
        'user': me,
        'my_jobs': Job.objects.filter(workers = me),
        'jobs' : Job.objects.exclude(workers = me),
    }
    return render(request, "jobs/index.html", context)
#
def add_job(request):
    return render(request, 'jobs/add_jobs.html')
#
def create_job(request):
    response = Job.objects.validateJob(request.POST, request.session['user_id'])
    if 'errors' in response:
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/jobs/add_job')
    return redirect('/jobs/')
#
def createJoin(request, job_id):
    me = User.objects.get(id=request.session['user_id'])
    job = Job.objects.get(id=job_id)
    job.workers.add(me)
    job.save()
    return redirect('/jobs')
#
def destroyJoin(request, job_id):
        me = User.objects.get(id=request.session['user_id'])
        job = Job.objects.get(id=job_id)
        job.workers.remove(me)
        job.save()
        return redirect('/jobs')
#
def show(request, job_id):
    job = Job.objects.get(id=job_id)
    context={
        'job': job,
        'users': User.objects.filter(planned_jobs=job).exclude(created_jobs=job)
    }
    return render(request, 'jobs/show.html', context)

def edit(request, job_id):
    request.session['job_id'] = job_id
    job = Job.objects.get(id=job_id)
    context={
        'job': job,
        'users': User.objects.filter(planned_jobs=job).exclude(created_jobs=job)
    }
    return render(request, 'jobs/edit.html', context)

def update(request, job_id):
    response = Job.objects.validateEdit(request.POST, job_id)
    if 'errors' in response:
        id = 'id'
        for error in response['errors']:
            messages.error(request, error)
        return redirect('/jobs/edit/{}'.format(job_id))
    return redirect('/jobs/')

def delete(request, job_id):
    Job.objects.get(id=job_id).delete()
    return redirect('/jobs')

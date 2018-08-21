from django.db import models
from ..login_app.models import User

# Create your models here.
class JobManager(models.Manager):
    def validateJob(self, postData, user_id):
        errors = []
        # check length of title
        if len(postData['title']) < 3:
            errors.append('Please enter a valid job title')
        # check length of description
        if len(postData['description']) < 10:
            errors.append('Your description is insufficient')
        # check if location exists
        if len(postData['location']) == 0:
            errors.append('Must provide a location')

        if len(errors) > 0:
            return {'errors': errors}
        else:
            me = User.objects.get(id=user_id)
            job = Job.objects.create(
                title = postData['title'],
                description = postData['description'],
                location = postData['location'],
                creator = User.objects.get(id=user_id)
            )
            job.workers.add(0)
            job.save()
            return {}
    def validateEdit(self, postData, job_id):
        errors = []
        # check length of title
        if len(postData['title']) < 3:
            errors.append('Please enter a valid job title')
        # check length of description
        if len(postData['description']) < 10:
            errors.append('Your description is insufficient')
        # check if location exists
        if len(postData['location']) == 0:
            errors.append('Must provide a location')

        if len(errors) > 0:
            return {'errors': errors, 'id':job_id}
        else:
            job = Job.objects.get(id=job_id)
            job.title = postData['title']
            job.description = postData['description']
            job.location = postData['location']
            job.save()
            return {}


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name = "created_jobs")
    workers = models.ManyToManyField(User, related_name = "planned_jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()

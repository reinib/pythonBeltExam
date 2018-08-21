from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

# Create your models here.
class UserManager(models.Manager):
    def validateUser(self, postData):
        errors = []
        # first name exists
        if len(postData['first_name']) == 0:
            errors.append('please enter a first name')
        #  last name exists
        if len(postData['last_name']) == 0:
            errors.append('please enter a first name')
        # email exists
        if len(postData['email']) == 0:
            errors.append('please enter an email')
        # is email correct format
        if not re.match('[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*@[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*(.[A-Za-z]{2,})', postData['email']):
            errors.append('This is not a valid email')
        # is email already registered
        if User.objects.filter(email=postData['email']):
            errors.append('This email is already being used')
        # check password
        if len(postData['password']) == 0:
            errors.append('please enter an password')
        if postData['password'] != postData['confirm_password']:
            errors.append('Password does not match')
        if len(errors) > 0:
            return {'errors': errors}
        else:
            user = User.objects.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()),
            )
            return {'user_id': user.id}

    def loginUser(self, postData):
        errors = []
        existing_user_list = User.objects.filter(email=postData['email'])
        if len(existing_user_list) == 1:
            if bcrypt.checkpw(postData['password'].encode(), existing_user_list[0].password.encode()):
                return {'user_id': existing_user_list[0].id}
            else:
                return {'errors': ['please endter a valid email / password combinaton']}
        else:
            return{'errors': ["please enter a valid email / password combinaton"]}
        return


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

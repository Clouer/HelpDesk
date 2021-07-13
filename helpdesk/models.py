from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = 'users'

    is_support = models.BooleanField(default=False)
    is_super_support = models.BooleanField(default=False)


class Department(models.Model):
    class Meta:
        db_table = 'departments'

    title = models.CharField(max_length=100)
    workers = models.ManyToManyField(User, related_name='departments')


class Request(models.Model):
    class Meta:
        db_table = 'requests'

    title = models.CharField(max_length=400)
    description = models.CharField(max_length=1500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    departments = models.ManyToManyField(Department, related_name='requests')


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    message = models.CharField(max_length=1500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='comments')

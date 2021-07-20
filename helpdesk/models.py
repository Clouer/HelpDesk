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

    def __str__(self):
        return self.title


class Request(models.Model):
    class Meta:
        db_table = 'requests'

    STATUS_CHOICES = (
        ('new', 'Новая'),
        ('in_work', 'В работе'),
        ('closed', 'Закрыта')
    )
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=1500)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='new')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    departments = models.ManyToManyField(Department, related_name='requests')

    def __str__(self):
        return f'Заявка № {self.id}: {self.title}'


class Comment(models.Model):
    class Meta:
        db_table = 'comments'

    message = models.CharField(max_length=1500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'Комментарий № {self.id} из заявки № {self.request}'

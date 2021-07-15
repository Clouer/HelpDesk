import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()  # Всякие Django штуки импортим после сетапа

from helpdesk.models import User, Request

if __name__ == '__main__':
    User.objects.create_user(
        first_name='System',
        last_name='admin',
        username='admin',
        password='admin',
        is_superuser=True,
        is_staff=True,
        is_support=True,
        is_super_support=True
    )
    User.objects.create_user(
        first_name='Обычный',
        last_name='Пользователь',
        username='user',
        password='user'
    )
    User.objects.create_user(
        first_name='Support',
        last_name='User',
        username='support',
        password='support',
        is_support=True
    )

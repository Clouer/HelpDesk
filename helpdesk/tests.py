import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'conf.settings'
django.setup()  # Всякие Django штуки импортим после сетапа

if __name__ == '__main__':
    pass

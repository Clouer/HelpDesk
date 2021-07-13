from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from helpdesk.models import User, Department, Request, Comment


class DepartmentsAdmin(admin.ModelAdmin):
    pass


class RequestsAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Department, DepartmentsAdmin)
admin.site.register(Request, RequestsAdmin)
admin.site.register(Comment, CommentsAdmin)

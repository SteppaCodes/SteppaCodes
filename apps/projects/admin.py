from django.contrib import admin

from .models import Project, Message

admin.site.register(Project)
admin.site.register(Message)

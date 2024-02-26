from django.db import models
from apps.common.models import BaseModel

PROJECT_TYPE_CHOICES = (
    ("API", "API"),
    ("FULL STACK", "FULL STACK"),
)

class Project(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=PROJECT_TYPE_CHOICES, default="API")
    image = models.ImageField(upload_to='projects images')
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


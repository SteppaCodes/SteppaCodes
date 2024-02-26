from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid

#Local imports
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars/", null=True)
    email = models.EmailField(_("Email Address"), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname"]

    #profile section
    dev_name = models.CharField(max_length=300)
    bio = models.TextField()
    insta = models.URLField(default="https://www.intagram.com")
    github = models.URLField(default="https://www.github.com")
    x = models.URLField(default="https://www.x.com")

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"
    
    def __str__(self):
        if self.dev_name:
            return self.dev_name
        return self.full_name

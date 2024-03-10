from django.shortcuts import render
from django.views import View
 
from apps.accounts.models import User
from .models import Project


class WebPageView(View):
    def get(self, request):
        user = User.objects.filter(dev_name="API Artist").first()
        projects = Project.objects.all()

        context = {
            "user": user, 
            "projects": projects
            }
        return render(request, "index.html", context)

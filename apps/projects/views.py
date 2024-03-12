from django.shortcuts import render, redirect
from django.views import View

from apps.accounts.models import User
from .models import Project
from .forms import MessageForm


class WebPageView(View):
    def get(self, request):
        user = User.objects.filter(dev_name="API Artist").first()
        projects = Project.objects.all()
        form = MessageForm()

        context = {"user": user, "projects": projects, "form": form}
        return render(request, "index.html", context)

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

        return render(request, "index.html", {"form": form})

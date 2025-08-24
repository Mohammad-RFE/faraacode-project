from django.shortcuts import render
from .models import Project
from footer_app.models import Footer, MessageForm


def show_projects(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        sub = request.POST.get("sub")
        message = request.POST.get("message")

        MessageForm.objects.create(name=name, email=email, sub=sub, message=message)

    projects = Project.objects.all()
    footer = Footer.objects.last()
    return render(request, "index.html", context={"projects": projects, "footer": footer})

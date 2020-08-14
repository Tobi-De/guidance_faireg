from django.shortcuts import render
from django.views.generic import CreateView

from .models import Parent, Student


def home(request):
    return render(request, "participants/home.html")


def confirmation(request):
    return render(request, "participants/confirmation.html")


class ParentRegisterView(CreateView):
    model = Parent
    fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "gender",
        "country",
        "city",
    ]
    success_url = "/confirmation"
    template_name = "participants/register.html"


class StudentRegisterView(CreateView):
    model = Student
    fields = [
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "gender",
        "bachelor_degree",
        "status",
        "country",
        "city",
    ]
    success_url = "/confirmation"
    template_name = "participants/register.html"

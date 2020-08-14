from django.shortcuts import render
from django.views.generic import CreateView

from .models import Parent, Student


def home(request):
    return render(request, "participants/home.html")


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
    template_name = "participants/register.html"

from django.shortcuts import render
from django.views.generic import CreateView

from .models import Parent, Student


def home(request):
    return render(request, "participants/home.html")


def confirmation(request, _type):
    if _type == "parent":
        msg = "Félicitation ! Votre compte est bien créé. Dans les jours à venir, " \
              "nous allons vous faire découvrir les universités béninoises et d'ailleurs " \
              "pour vos enfants. Vous aurez aussi accès à des conférences d'orientations. " \
              "Cordialement, l'équipe de E-DEV Technologies."
    else:
        msg = "Félicitation ! Votre compte est bien créé. Dans les jours à venir, " \
              "nous allons vous faire découvrir les universités béninoises et d'ailleurs. " \
              "Vous aurez aussi accès à des conférences d'orientations. Cordialement, l'équipe " \
              "de E-DEV Technologies"
    return render(request, "participants/confirmation.html", {"msg": msg})


class ParentRegisterView(CreateView):
    model = Parent
    fields = [
        "last_name",
        "first_name",
        "email",
        "phone_number",
        "gender",
        "country",
        "city",
    ]
    success_url = "/confirmation/parent/"
    template_name = "participants/register.html"


class StudentRegisterView(CreateView):
    model = Student
    fields = [
        "last_name",
        "first_name",
        "email",
        "phone_number",
        "gender",
        "bachelor_degree",
        "status",
        "country",
        "city",
    ]
    success_url = "/confirmation/student/"
    template_name = "participants/register.html"

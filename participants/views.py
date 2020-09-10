from django.shortcuts import render
from django.views.generic import CreateView

from .forms import ParentRegisterForm, StudentRegisterForm
from .models import Parent, Student


def home(request):
    return render(request, "participants/home.html")


def confirmation(request, _type):
    if _type == "parent":
        msg = "Félicitation chère parent! Votre compte est bien créé. " \
              "Dans les jours à venir, nous allons vous faire découvrir " \
              "les universités béninoises et d'ailleurs. Vous aurez aussi " \
              "accès à des conférences d'orientations. accompagnez votre " \
              "enfant dans le choix de son école.Cordialement, l'équipe de E-DEV Technologies"
    else:
        msg = "Félicitation ! Votre compte est bien créé. Dans les jours à venir, " \
              "nous allons vous faire découvrir les universités béninoises et d'ailleurs. " \
              "Vous aurez aussi accès à des conférences d'orientations. Cordialement, l'équipe " \
              "de E-DEV Technologies"
    return render(request, "participants/confirmation.html", {"msg": msg})


class ParentRegisterView(CreateView):
    model = Parent
    form_class = ParentRegisterForm
    success_url = "/confirmation/parent/"
    template_name = "participants/register.html"


class StudentRegisterView(CreateView):
    model = Student
    form_class = StudentRegisterForm
    success_url = "/confirmation/student/"
    template_name = "participants/register.html"

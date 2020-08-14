from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel

from .validators import validate_phone_number


class Participant(TimeStampedModel):
    SEXE_CHOICES = Choices("Homme", "Femme")
    first_name = models.CharField("Prénoms", max_length=120)
    last_name = models.CharField("Nom", max_length=60)
    email = models.EmailField()
    phone_number = models.CharField("Tél", max_length=100, validators=[validate_phone_number])
    gender = models.CharField("Sexe", max_length=6, choices=SEXE_CHOICES)
    country = models.CharField("Pays", max_length=60)
    city = models.CharField("Ville", max_length=60)

    class Meta:
        abstract = True

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"


class Parent(Participant):
    pass


class Student(Participant):
    STATUS = Choices("bachelier", "étudiant")
    bachelor_degree = models.CharField("Série de Bac", max_length=5)
    status = models.CharField(choices=STATUS, max_length=12)

from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Participant(TimeStampedModel):
    SEXE_CHOICES = Choices("Homme", "Femme")
    first_name = models.CharField("Prénoms", max_length=120)
    last_name = models.CharField("Nom", max_length=60)
    email = models.EmailField()
    phone_number = models.CharField("Tél", max_length=20)
    gender = models.CharField(
        "Sexe", max_length=6, choices=SEXE_CHOICES, default=SEXE_CHOICES.Homme
    )
    country = models.CharField("Pays", max_length=60)
    city = models.CharField("Ville", max_length=60)

    class Meta:
        abstract = True

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return self.full_name


class Parent(Participant):
    pass


class Student(Participant):
    STATUS = Choices("bachelier", "étudiant")
    BACHELOR_DEGREE_CHOICES = Choices("A", "B", "C", "D", "G1", "G2", "G3", "F")
    bachelor_degree = models.CharField(
        "Série de Bac",
        max_length=5,
        choices=BACHELOR_DEGREE_CHOICES,
        default=BACHELOR_DEGREE_CHOICES.A,
    )
    status = models.CharField(choices=STATUS, max_length=12, default=STATUS.bachelier)

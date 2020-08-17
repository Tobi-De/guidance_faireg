from django import forms

from .models import Student, Parent


# class RegistrationForm:
#
#     def clean_email(self):
#         email = self.cleaned_data["email"]
#         if is_valid_email(email):
#             return forms.ValidationError("cet email semble invalide pour le moment, "
#                                          "veuillez réessayer s'il vous plait ou entrer "
#                                          "un autre email, si le problème persiste, "
#                                          "contactez-nous s'il vous plaît")
#         else:
#             return email


class ParentRegisterForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

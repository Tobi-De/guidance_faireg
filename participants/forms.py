from django import forms

from .models import Student, Parent


class ParentRegisterForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

from django.contrib import admin

from .models import Student, Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

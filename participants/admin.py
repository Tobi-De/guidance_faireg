from django.contrib import admin

from .models import Student, Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    search_fields = ["email", "last_name"]
    list_display = [
        "last_name",
        "first_name",
        "email",
        "phone_number",
        "gender",
        "country",
        "city",
    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ["email", "last_name"]
    list_display = [
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

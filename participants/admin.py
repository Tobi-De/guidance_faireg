from django.contrib import admin
from django.http import HttpResponse

from .models import Student, Parent
from .utils import queryset_to_csv


class DownloadCSVMixin:

    @property
    def file_name(self):
        raise NotImplemented

    def download_as_csv(self, request, queryset):
        file = queryset_to_csv(queryset)
        response = HttpResponse(file, content_type="text/csv")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={self.file_name}.csv"
        return response

    download_as_csv.short_description = "Telecharger en csv"


@admin.register(Parent)
class ParentAdmin(DownloadCSVMixin, admin.ModelAdmin):
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
    file_name = "parents"


@admin.register(Student)
class StudentAdmin(DownloadCSVMixin, admin.ModelAdmin):
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
    file_name = "students"

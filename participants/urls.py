from django.urls import path

from .views import home, ParentRegisterView, StudentRegisterView

app_name = "participants"
urlpatterns = [
    path("", home, name="home"),
    path("register/parent/", ParentRegisterView.as_view(), name="parent_register"),
    path("register/student/", StudentRegisterView.as_view(), name="student_register")
]

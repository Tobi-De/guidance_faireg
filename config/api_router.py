from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from guidance_faireg.users.api.views import UserViewSet
from participants.api.viewsets import ParentViewset, StudentViewset

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"users", UserViewSet)
router.register(r"parents", ParentViewset)
router.register(r"students", StudentViewset)

app_name = "api"
urlpatterns = router.urls

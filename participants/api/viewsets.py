from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import ParentSerializer, StudentSerializer
from ..models import Parent, Student


class ParentViewset(ReadOnlyModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


class StudentViewset(ReadOnlyModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

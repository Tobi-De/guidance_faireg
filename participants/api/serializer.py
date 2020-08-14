from rest_framework import serializers

from ..models import Parent, Student


class ParentSerializer(serializers.ModelSerialize):
    class Meta:
        model = Parent


class StudentSerializer(serializers.ModelSerialize):
    class Meta:
        model = Student

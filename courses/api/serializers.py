from rest_framework import serializers
from ..models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """
    serializer to serialize Subject model objects
    """
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']

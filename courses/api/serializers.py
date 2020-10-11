from rest_framework import serializers
from ..models import Subject, Course, Module


class SubjectSerializer(serializers.ModelSerializer):
    """
    serializer to serialize Subject model objects
    """
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSerializer(serializers.ModelSerializer):
    """
    serializer for Module objects
    """
    class Meta:
        model = Module
        fields = ['title', 'description', 'order']


class CourseSerializer(serializers.ModelSerializer):
    """
    serializer for Course model objects
    """
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner', 'modules']

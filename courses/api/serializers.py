from rest_framework import serializers
from ..models import Subject, Course, Module, Content


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


class ItemRelatedField(serializers.RelatedField):
    """
    serializer for different types of Content item
    uses custom render() method to provide rendered API
    """

    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    """
    serializer for Content model objects
    """
    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'item']


class ModuleWithContentSerializer(serializers.ModelSerializer):
    """
    serializer for Module with contents
    """
    class Meta:
        model = Module
        fields = ['order', 'title', 'dscription', 'contents']


class CourseWithContentSerializer(serializers.ModelSerializer):
    """
    serializer for Course with Contents
    """

    class Meta:
        model = Course
        fields = ['id', 'subject', 'title', 'slug',
                  'overview', 'created', 'owner', 'modules']

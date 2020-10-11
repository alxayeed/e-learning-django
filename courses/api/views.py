from rest_framework import generics
from ..models import Subject, Course
from .serializers import SubjectSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class SubjectListView(generics.ListAPIView):
    """
    API view for handling Subject list
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    """
    API view for handling Subject Details
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
    """
    custom API view to handle student enrollment
    """

    def post(self, request, pk, format=None):
        course = Course.get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})

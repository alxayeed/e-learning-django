from rest_framework import generics, viewsets
from ..models import Subject, Course
from .serializers import SubjectSerializer, CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


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

# this view is replaced by CourseViewSet

# class CourseEnrollView(APIView):
#     """
#     custom API view to handle student enrollment
#     """
#     authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled': True})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True,
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

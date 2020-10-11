from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer


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

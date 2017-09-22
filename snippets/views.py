from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer

@method_decorator(csrf_exempt, name="dispatch")
class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

@method_decorator(csrf_exempt, name="dispatch")
class SnippetDetail(generics.ListCreateAPIView):
    """
    Retrieve, update or delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .models import Quiz
from .serializers import QuizSerializer
# Create your views here.
class QuizzViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
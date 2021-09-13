from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import Habit
from .serializers import HabitSerializer

class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
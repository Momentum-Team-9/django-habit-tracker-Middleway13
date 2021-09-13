from django.contrib.auth.models import User
from core.models import Habit
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    goal = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Habit
        fields = ('pk', 'goal', 'created_date', 'created_by',)
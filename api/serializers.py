from django.contrib.auth.models import User
from core.models import Habit
from rest_framework import serializers

class HabitSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field="user", read_only=True)
    goals = serializers.StringRelatedField(slug_field="goal", read_only=True)
    
    class Meta:
        model = Habit
        fields = ('pk', 'goal', 'created_date', 'created_by',)
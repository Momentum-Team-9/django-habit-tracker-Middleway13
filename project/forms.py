from django import forms
from core.models import Habit, DailyResult


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['goal', 'created_date']


class DailyResultForm(forms.ModelForm):
    class Meta:
        model = DailyResult
        fields = ['habit', 'results', 'date']
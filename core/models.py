from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db.models.constraints import UniqueConstraint

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Habit(models.Model):
    goal = models.CharField(max_length=100)
    target = models.TextField()
    created_date = models.DateField(default=date.today)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='habits')
    
    def __str__(self):
        return f"{self.goal}"

class DailyResult (models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='results', null=True)
    results = models.PositiveIntegerField()
    date = models.DateField(default=date.today)
    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='daily_record')
        ]
        
        def __str__(self):
            return f"{self.date} {self.habit}"

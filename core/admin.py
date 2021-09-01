from django.contrib import admin
from .models import User, Habit, DailyResult

admin.site.register(User)
admin.site.register(Habit)
admin.site.register(DailyResult)
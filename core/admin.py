from django.contrib import admin
from .models import User, Habit, DailyResult

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ['goal', 'created_date', 'created_by']

@admin.register(DailyResult)
class DailyResultAdmin(admin.ModelAdmin):
    pass
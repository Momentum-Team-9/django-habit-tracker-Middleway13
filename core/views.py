from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from core.models import Habit, DailyResult
from project.forms import HabitForm


def home(request):
    if request.user.is_authenticated:
        return redirect(to='list_habits')
    return render(request, 'habits/home.html')

@login_required
def list_habits(request):
    user = request.user
    habits = Habit.objects.filter(created_by=user)
    return render(request, 'habits/list_habits.html', {'habits': habits})

@login_required
def view_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(
        request, 'habits/view_habit.html', {'habit': habit, 'pk': pk})
    
@login_required
def new_habit(request):
    if request.method == 'POST':
        filled_form = HabitForm(request.POST)
        if filled_form.is_valid():
            note = 'New habit successfully created!' %(filled_form.cleaned_data['goal'])
            new_form = HabitForm()
            return render(request, 'habits/new_habit.html', {'form': new_form, 'note':note})
    else:
        form = HabitForm()
        return render(request, 'habits/new_habit.html', {'form': form})
    
    
    
    
    
    
    
#    if request.method == "GET":
#        form = HabitForm()
#    else:
#        form = HabitForm(data=request.POST)
#        if form.is_valid():
#            habit = form.save(commit=False)
#            habit.save()
#            return redirect(to="list_habits")
#
#    return render(request, "habits/new_habit.html", {"form": form})
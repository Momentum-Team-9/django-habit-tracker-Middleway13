from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from core.models import User, Habit, DailyResult
from project.forms import HabitForm, DailyResultForm


def home(request):
    users = User.objects.all()
    if request.user.is_authenticated:
        return redirect(to='list_habits')
    return render(request, 'habits/home.html', {'users': users})

@login_required
def list_habits(request):
    user = request.user
    habits = Habit.objects.filter()
    return render(request, 'habits/list_habits.html', {'habits': habits})

@login_required
def view_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'habits/view_habit.html', {'habit': habit, 'pk': pk})
    
@login_required
def new_habit(request):
    if request.method == 'GET':
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.save()
#           messages.success(request, 'New habit successfully created!')
            return redirect('list_habits')
        
    return render(request, 'habits/new_habit.html', {'form': form})
    
@login_required
def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect('list_habits')

    return render(request, 'habits/delete_habit.html', {'habit': habit})

@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect(to="list_habits")

    return render(
        request, "habits/edit_habit.html", {"form": form, "habit": habit})
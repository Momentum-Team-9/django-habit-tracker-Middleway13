from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from core import views as habit_views

urlpatterns = [
    path('', habit_views.home, name='home'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('habits/', habit_views.list_habits, name='list_habits'),
    path('habits/<int:pk>/', habit_views.view_habit, name='view_habit'),
    path('habits/new', habit_views.new_habit, name='new_habit'),
    path('habits/<int:pk>/delete/', habit_views.delete_habit, name='delete_habit'),
    path('habits/<int:pk>/edit/', habit_views.edit_habit, name='edit_habit'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),    
    ] + urlpatterns

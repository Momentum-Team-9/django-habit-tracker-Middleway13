from django.contrib import admin
from django.conf import settings
from django.urls import include, path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('habits/', views.list_habits, name='list_habits'),
    path('habits/<int:pk/', views.view_habit, name='view_habit'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        
        
    ] + urlpatterns

from django.urls import path

from . import views

urlpatterns = [
    path('get_active_courses/', views.get_active_courses),
]
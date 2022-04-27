from django.urls import path

from . import views

urlpatterns = [
    path('get_active_courses/', views.get_active_courses),
    path('track_started/<slug:course_slug>/<slug:lesson_slug>/', views.track_started),
    path('mark_as_done/<slug:course_slug>/<slug:lesson_slug>/', views.mark_as_done),
]
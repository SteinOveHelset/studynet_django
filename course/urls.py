from django.urls import path

from course import views

urlpatterns = [
    path('', views.get_courses),
    path('<slug:slug>/', views.get_course),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_student, name='home'),  # Default page opens search
    path('register/', views.register_student, name='register_student'),
    path('search/', views.search_student, name='search_student'),
]

from django.urls import path

from .import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('todos/details/<id>/', views.details),
    path('add/', views.add, name = 'add')
]

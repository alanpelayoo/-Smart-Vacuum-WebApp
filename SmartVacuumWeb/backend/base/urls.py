
from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('status/', views.getStatus, name="status"),
    path('sensors/', views.getSensors, name="sensors"),
    path('sensors/<str:pk>/', views.getSensor, name="sensor"),
]
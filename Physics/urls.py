from django.urls import path
from . import views

urlpatterns = [
    path('', views.physics, name="physics"),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.latex_input, name="latex_input"),
    path('output', views.latex_output, name="latex_output"),
]
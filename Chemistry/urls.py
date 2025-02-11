from django.urls import path
from . import views

urlpatterns = [
    path('', views.chemistry, name="chemistry"),

]
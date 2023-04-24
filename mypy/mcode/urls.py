from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', compiler,name="compiler"),
    path("run",runn,name="runn"),
]
 
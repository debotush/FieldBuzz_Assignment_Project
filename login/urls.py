from django.urls import path
from . import views, loginController

urlpatterns = [
    path('', views.index)
]

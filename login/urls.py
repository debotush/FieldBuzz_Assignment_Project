from django.urls import path
from . import views, loginAPIService

urlpatterns = [
    path('', views.index)
]

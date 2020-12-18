from django.urls import path
from . import views, recruitmentAPIService

urlpatterns = [
    path('', views.recruitment_index)
]


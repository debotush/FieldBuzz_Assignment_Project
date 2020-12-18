from django.urls import path
from . import views, recruitmentController

urlpatterns = [
    path('', views.recruitment_index)
]


from django.urls import path
from . import views, loginController

urlpatterns = [
    path('', views.index),
    path('login/', loginController.login_con)
]

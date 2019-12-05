from django.urls import path

from .views import signup as signup_view
from .views import client as client_view

urlpatterns = [
    path('clients:signup/', signup_view.SignUpView.as_view(), name='clients.signup'),
    path('clients/me/urls/', client_view.URLView.as_view(), name='urls.getOrCreate'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('auth/tokens/', views.TokenView.as_view(), name='tokens.create'),
]
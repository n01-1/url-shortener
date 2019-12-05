from django.urls import path

from . import views

urlpatterns = [
    path('links/<url>/', views.LinkView.as_view(), name='links.get'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('analytics/today-reports/', views.TodayStatisticsView.as_view()),
    path('analytics/yesterday-reports/', views.YesterdayStatisticsView.as_view()),
    path('analytics/week-reports/', views.WeekStatisticsView.as_view()),
    path('analytics/month-reports/', views.MonthStatisticsView.as_view()),
]

from django.urls import path

from main_task.views import MainStatsView

urlpatterns = [
    path("stats/", MainStatsView.as_view(), name="stats")
]

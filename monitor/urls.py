from django.urls import path
from .views import ProcessDataView

urlpatterns = [
    path('process-data/', ProcessDataView.as_view()),  # all processes
    path('process-data/<str:hostname>/', ProcessDataView.as_view()),  # specific hostname
]
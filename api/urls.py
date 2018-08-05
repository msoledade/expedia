from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('processes/', views.ProcessList.as_view()),
    path('process/<pk>', views.ProcessDetail.as_view()),
]

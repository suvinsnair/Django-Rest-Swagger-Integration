# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from django.views.generic import TemplateView


urlpatterns = [
    path('list/', views.AcConfigurationList.as_view()),
    path('set/humidity/', views.AcConfigurationSetHumidity.as_view()),
    path('get/humidity/', views.AcConfigurationGetHumidity.as_view()),
]
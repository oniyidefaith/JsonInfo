from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.json_data_info, name='info'),
]

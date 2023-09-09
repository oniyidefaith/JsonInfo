from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/?$', views.json_data_info, name='get_info'),
]

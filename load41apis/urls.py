from . import views
from django.urls import path
from .views import trackers_info_list
from .views import trackers_info_by_id

urlpatterns = [
    path('', views.home, name="home"),
    path('trackers-info/', trackers_info_list, name='trackers-info-list'),
    path('trackers-info/<str:trackers_info_id>/', trackers_info_by_id, name='trackers-info-by-id'),
]

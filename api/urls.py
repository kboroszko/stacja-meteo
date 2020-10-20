from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:station_id>/get_data', views.get_data),
    path('<int:station_id>/post_data', views.post_data),
    path('stations', views.get_stations),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('filter-hotel-by-name/', filter_hotel_by_name),
    path('filter-hotel-by-rating/', filter_hotel_by_rating),
    path('filter-restoran-by-rating/', filter_restoran_by_rating),
    path('filter-menu-by-name/', filter_menu_by_name),
    path('filter-restoran-by-name/', filter_restoran_by_name),
    path('filter-hotel-by-address/', filter_hotel_by_address),
    path('filter-room-by-capicaty/', filter_room_by_capicaty),
    path('filter-achievement-by-name/', filter_achievement_by_name),
]
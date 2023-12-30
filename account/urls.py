from django.urls import path
from .views import *

urlpatterns=[
    path('get-region/', GetRegion),
    path('get-restoran/', GetRestoran),
    path('get-menu/', GetMenu),
    path('get-menuitem/', GetMenuItem),
    path('get-order/', GetOrder),
    path('get-table/', GetTable),
    path('get-reservation/', GetReservation_table),
    path('get-hotel/', GetHotel),
    path('get-room/', GetRoom),
    path('get-services/', GetServices),
    path('get-achiavement/', GetAchiavement),
    path('get-language/', GetLanguage),
    path('get-git/', GetGit),
    path('get-order-room/', GetOrder_room),
    path('get-employee/', GetEmployee),
]
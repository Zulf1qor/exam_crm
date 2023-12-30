from django.urls import path
from .views import *


urlpatterns = [
    path('create-region/', CreateRegion.as_view()),
    path('update-region/<int:pk>/', UpdateRegion.as_view()),
    path('delete-region/<int:pk>/', DeleteRegion.as_view()),

    path('create-restoran/', CreateRestoran.as_view()),
    path('update-restoran/<int:pk>/', UpdateRestoran.as_view()),
    path('delete-restoran/<int:pk>/', DeleteRestoran.as_view()),

    path('create-menu/', CreateMenu.as_view()),
    path('update-menu/<int:pk>/', UpdateMenu.as_view()),
    path('delete-menu/<int:pk>/', DeleteMenu.as_view()),

    path('create-menuitem/', CreateMenuItem.as_view()),
    path('update-menuitem/<int:pk>/', UpdateMenuItem.as_view()),
    path('delete-menuitem/<int:pk>/', DeleteMenuItem.as_view()),

    path('create-order/', CreateOrder.as_view()),
    path('update-order/<int:pk>/', UpdateOrder.as_view()),
    path('delete-order/<int:pk>/', DeleteOrder.as_view()),

    path('create-table/', CreateTable.as_view()),
    path('update-table/<int:pk>/', UpdateTable.as_view()),
    path('delete-table/<int:pk>/', DeleteTable.as_view()),

    path('create-reservation_table/', CreateReservetion_table.as_view()),
    path('update-reservetion_table/<int:pk>/', UpdateReservetion_table.as_view()),
    path('delete-reservetion_table/<int:pk>/', DeleteReservetion_table.as_view()),

    path('create-hotel/', CreateHotel.as_view()),
    path('update-hotel/<int:pk>/', DeleteHotel.as_view()),
    path('delete-hotel/<int:pk>/', DeleteHotel.as_view()),

    path('create-room/', CreateRoom.as_view()),
    path('update-room/<int:pk>/', UpdateRoom.as_view()),
    path('delete-room/<int:pk>/', DeleteRoom.as_view()),

    path('create-service/', CreateService.as_view()),
    path('update-service/<int:pk>/', DeleteService.as_view()),
    path('delete-service/<int:pk>/', DeleteService.as_view()),

    path('create-achievement/', CreateAchievement.as_view()),
    path('update-achievement/<int:pk>/', UpdateAchievement.as_view()),
    path('delete-achievement/<int:pk>/', DeleteAchievement.as_view()),

    path('edit-user/', edit_user_view),
    path('delete-user/<int:pk>/', delete_user),
    path('singup-view/', singup_view),
    path('login_view/', login_view),
    path('logout_view/', logout_view),

    path('create-language/', CreateLanguage.as_view()),
    path('update-language/<int:pk>/', UpdateLanguage.as_view()),
    path('delete-language/<int:pk>/', DeleteLanguage.as_view()),

    path('create-git/', CreateGit.as_view()),
    path('update-git/<int:pk>/', UpdateGit.as_view()),
    path('delete-git/<int:pk>/', DeleteGit.as_view()),

    path('create-Order_room/', CreateOrder_room.as_view()),
    path('update-Order_room/<int:pk>/', UpdateOrder_room.as_view()),
    path('delete-Order_room/<int:pk>/', DeleteOrder_room.as_view()),

    path('create-employee/', CreateEmployee.as_view()),
    path('update-employee/<int:pk>/', UpdateEmployee.as_view()),
    path('delete-employee/<int:pk>/', DeleteEmployee.as_view())

]



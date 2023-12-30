from django.shortcuts import render
from main.models import *
from main.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView



@api_view(['GET'])
def GetRegion(request):
    region = Region.objects.all()
    ser = RegionSerializer(region, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetRestoran(request):
    restoran = Restoran.objects.all()
    ser = RestoranSerializers(restoran, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetMenu(request):
    menu = Menu.objects.all()
    ser = MenuSerializers(menu, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetMenuItem(request):
    menuitem = MenuItem.objects.all()
    ser = MenuItemSerializers(menuitem, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetOrder(request):
    order = Order.objects.all()
    ser = OrderSerializers(order, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetTable(request):
    table = Table.objects.all()
    ser = TableSerializers(table, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetReservation_table(request):
    reservation = Reservetion_table.objects.all()
    ser = Reservetion_tableSerializers(reservation, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetHotel(request):
    hotel = Hotel.objects.all()
    ser = HotelSerializers(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetRoom(request):
    room = Room.objects.all()
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetServices(request):
    service = Service.objects.all()
    ser = ServiceSerializers(service, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetAchiavement(request):
    achievement = Achievement.objects.all()
    ser = Achievement(achievement, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetLanguage(request):
    language = Language.objects.all()
    ser = LanguageSerializers(language, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetGit(request):
    git = Git.objects.all()
    ser = GitSerializers(git, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetOrder_room(request):
    order_room = Order_room.objects.all()
    ser = Order_roomSerializers(order_room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetEmployee(request):
    employee = Employee.objects.all()
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)

from django.shortcuts import render
from main.models import *
from main.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView


@api_view(['POST'])
def filter_hotel_by_name(reqeust):
    name = reqeust.POST('name')
    hotel = Hotel.objects.filter(name__icontains=name)
    ser = HotelSerializers(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_hotel_by_rating(request):
    hotel = Hotel.objects.all().order_by('-rating')[:10]
    ser = HotelSerializers(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_restoran_by_rating(request):
    restoran = Restoran.objects.all().order_by('-rating')[:10]
    ser = RestoranSerializers(restoran, many=True)
    return Response(ser.data)


@api_view(['POST'])
def filter_menu_by_name(request):
    name = request.POST('name', )
    menu = Menu.objects.filter(name__icontains=name)
    ser = MenuSerializers(menu, many=True)
    return Response(ser.data)


@api_view(['POST'])
def filter_restoran_by_name(request):
    name = request.POST('name', )
    restoran = Restoran.objects.filter(name__icontains=name)
    ser = RestoranSerializers(restoran, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_hotel_by_address(request):
    hotel = Hotel.objects.all().order_by('-address')[:10]
    ser = HotelSerializers(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_room_by_capicaty(request):
    room = Room.objects.all().order_by('-capicaty')[:10]
    ser = RoomSerializers(room, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_achievement_by_name(request):
    achievement = Achievement.objects.all().order_by('-name')[:10]
    ser = AchievementSerializers(achievement, many=True)
    return Response(ser.data)


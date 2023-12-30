from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class RestoranSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restoran
        fields = "__all__"


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class Reservetion_tableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservetion_table
        fields = "__all__"


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class AchievementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"


class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class GitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Git
        fields = "__all__"


class Order_roomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order_room
        fields = "__all__"


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"




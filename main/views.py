from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView


"""  Start Region CRUD  """

class CreateRegion(ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class UpdateRegion(UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DeleteRegion(DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

""" End Region CRUD  """


"""  Star Restoran CRUD  """

class CreateRestoran(ListCreateAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranSerializers


class UpdateRestoran(UpdateAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranSerializers


class DeleteRestoran(DestroyAPIView):
    queryset = Restoran.objects.all()
    serializer_class = RestoranSerializers

""" End Restoran CRUD  """



""" Start User CRUD """
@api_view(['POST'])
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                status = 200
                data = {
                    'status': status,
                    'username': username
                }
            else:
                status = 403
                message = " Invalid Password or Username! "
                data = {
                    'status': status,
                    'message': message
                }
        except User.DoesNotExist:
            status = 404
            message = "This User is not defined! "
            data = {
                'status': status,
                'message': message
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def singup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone_number')
    new = User.objects.create_user(
        username=username,
        password=password,
        phone_number=phone_number,
    )
    ser = UserSerializer(new)
    return Response(ser.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'data': 'sucses'})


@api_view(['PUT'])
def edit_user_view(request, pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            username = request.data.get('username')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            address = request.data.get('address')
            phone_number = request.data.get('phone_number')
            password = request.data.get('password')
            if username is not None:
                user.username = username
            if first_name is not None:
                user.first_name = first_name
            if last_name is not None:
                user.last_name = last_name
            if email is not None:
                user.email = email
            if address is not None:
                user.address_id = address
            if phone_number is not None:
                user.phone_number = phone_number
            if password is not None:
                user.set_password(password)
            user.save()
            ser = UserSerializer(user)
            return Response(ser.data)
        except:
            status = 404
            message = "Request failed"
            data = {
                'status': status,
                'message': message,
            }
    except:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['DELETE'])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        data = {
            'message': "User deleted successfully"
        }
    except:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)

""" End User CRUD """



"""  Start Menu CRUD  """

class CreateMenu(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class UpdateMenu(UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class DeleteMenu(DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

""" End Menu CRUD  """



"""  Start MenuItem CRUD  """

class CreateMenuItem(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers


class UpdateMenuItem(UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers


class DeleteMenuItem(DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers

""" End MenuItem CRUD  """



"""  Start Order CRUD  """

class CreateOrder(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class UpdateOrder(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class DeleteOrder(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

""" End Order CRUD  """



"""  Start Table CRUD  """

class CreateTable(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializers


class UpdateTable(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializers


class DeleteTable(DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializers

""" End Table CRUD  """



"""  Start Reservetion_table CRUD  """

class CreateReservetion_table(ListCreateAPIView):
    queryset = Reservetion_table.objects.all()
    serializer_class = Reservetion_tableSerializers


class UpdateReservetion_table(UpdateAPIView):
    queryset = Reservetion_table.objects.all()
    serializer_class = Reservetion_tableSerializers


class DeleteReservetion_table(DestroyAPIView):
    queryset = Reservetion_table.objects.all()
    serializer_class = Reservetion_tableSerializers

""" End Reservetion_table CRUD  """




"""  Start Hotel CRUD  """

class CreateHotel(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers


class UpdateHotel(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers


class DeleteHotel(DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

""" End Hotel CRUD  """



"""  Start Room CRUD  """

class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class UpdateRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

""" End Room CRUD  """



"""  Start Service CRUD  """

class CreateService(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers


class UpdateService(UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers


class DeleteService(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers

""" End Service CRUD  """



"""  Start Achievement CRUD  """

class CreateAchievement(ListCreateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializers


class UpdateAchievement(UpdateAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializers


class DeleteAchievement(DestroyAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializers

""" End Achievement CRUD  """



"""  Start Language CRUD  """

class CreateLanguage(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers


class UpdateLanguage(UpdateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers


class DeleteLanguage(DestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers

""" End Language CRUD  """



"""  Start Git CRUD  """

class CreateGit(ListCreateAPIView):
    queryset = Git.objects.all()
    serializer_class = GitSerializers


class UpdateGit(UpdateAPIView):
    queryset = Git.objects.all()
    serializer_class = GitSerializers


class DeleteGit(DestroyAPIView):
    queryset = Git.objects.all()
    serializer_class = GitSerializers

""" End Git CRUD  """



"""  Start Order_room CRUD  """

class CreateOrder_room(ListCreateAPIView):
    queryset = Order_room.objects.all()
    serializer_class = Order_roomSerializers


class UpdateOrder_room(UpdateAPIView):
    queryset = Order_room.objects.all()
    serializer_class = Order_roomSerializers


class DeleteOrder_room(DestroyAPIView):
    queryset = Order_room.objects.all()
    serializer_class = Order_roomSerializers

""" End Order_room CRUD  """




"""  Start Employee CRUD  """

class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

""" End Employee CRUD  """




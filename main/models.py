from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Region(models.Model):
    name = models.CharField(max_length=255)


class User(AbstractUser):
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])

    class Meta(AbstractUser.Meta):
        swappable  = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def __str__(self):
        return self.username



class Restoran(models.Model):
    restoran_name = models.CharField(max_length=55)
    description = models.TextField()
    state = models.CharField(max_length=55)
    province = models.CharField(max_length=155)
    region = models.CharField(max_length=155)
    lot = models.FloatField()
    lat = models.FloatField()
    image = models.ImageField(upload_to='Restoran_photo/')
    services = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.restoran_name


class Menu(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    price = models.CharField(max_length=255, default=0)
    category_id = models.ForeignKey(to='Menu', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    last_name = models.CharField(max_length=155)
    region = models.ForeignKey(to='Region', on_delete=models.PROTECT)
    lot = models.FloatField()
    lat = models.FloatField()
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])

    def __str__(self):
        return self.last_name


class Table(models.Model):
    table_number = models.CharField(max_length=155)
    capicaty = models.IntegerField()
    status = models.CharField(max_length=255)


class Reservetion_table(models.Model):
    reservetion = models.ForeignKey(to='Table', on_delete=models.CASCADE)

    def __str__(self):
        return self.reservetion



class Hotel(models.Model):
    name = models.CharField(max_length=255)
    open_time = models.DateTimeField()
    address = models.TextField()
    lot = models.FloatField()
    lat = models.FloatField()
    image = models.ImageField(upload_to='hotel_photo/')
    free_wifi = models.BooleanField(default=False)
    free_porkovka = models.BooleanField(default=False)
    laundry_facilities = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=155)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10)


    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=155)
    photo = models.ImageField(upload_to='room_photo/')
    size = models.CharField(max_length=255)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.hotel


class Service(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    img = models.ImageField(upload_to="sevrive_img")


class Achievement(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    img = models.ImageField(upload_to="yutuq_img/")


class Language(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Git(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(default=18)
    languge = models.ManyToManyField(to="Language")
    experience = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to="git_img/")
    slug = models.SlugField(max_length=40, unique=True, blank=False)


class Order_room(models.Model):
    fist_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    address = models.CharField(max_length=55)
    people_number = models.IntegerField()
    is_delivery = models.BooleanField(default=False)
    TYPE_CHOICES = (
        ('luks', 'luks'),
        ('simple', 'simple')
    )
    room = models.CharField(max_length=25, choices=TYPE_CHOICES)
    date = models.DateField()



class Employee(models.Model):
    user = models.ForeignKey(to="User", on_delete=models.CASCADE)
    status = models.IntegerField(default=5, choices=(
        (1, 'direktor'),
        (2, 'manager'),
        (3, 'admin'),
        (4, 'worker'),
        (5, 'other'),
    ))
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()















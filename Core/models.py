from django.db import models
from django.contrib.auth.models import User


car_categories = (
    ("T", "Toyota"),
    ("V", "Volkswagen Group"),
    ("G", "General Motors"),
    ("F", "Ford Motor Company"),
    ("H", "Honda"),
    ("N", "Nissan"),
    ("HY", "Hyundai Motor Group"),
    ("BM", "BMW Group"),
    ("MB", "Mercedes-Benz"),
    ("TSLA", "Tesla, Inc."),
    ("FCA", "Fiat Chrysler Automobiles (now part of Stellantis)"),
    ("ST", "Stellantis (formed by the merger of FCA and PSA Group)"),
    ("SU", "Subaru (a division of Subaru Corporation)"),
    ("K", "Kia Motors Corporation"),
    ("M", "Mazda"),
    ("RG", "Renault Group (part of the Renault-Nissan-Mitsubishi Alliance)"),
    ("MM", "Mitsubishi Motors (part of the Renault-Nissan-Mitsubishi Alliance)"),
    ("VC", "Volvo Cars (owned by Geely Holding Group)"),
    ("TM", "Tata Motors"),
    ("SAIC", "SAIC Motor Corporation"),
    ("GH", "Geely Holding Group"),
    ("BYD", "BYD Auto"),
    ("CA", "Changan Automobile"),
    ("GW", "Great Wall Motors"),
    ("DMC", "Dongfeng Motor Corporation"),
    ("SMC", "Suzuki Motor Corporation"),
)

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    picture = models.ImageField(upload_to='products',
                                height_field=None, width_field=None, max_length=100, default=0)
    description = models.TextField(max_length=500)
    model = models.CharField(max_length=5, choices=car_categories,
                             blank=True, default='Toyota',)
    product_date = models.DateField()
    published_date = models.DateTimeField(auto_now_add=True)
    Price = models.FloatField(max_length=10, default=0)
    fuel_efficiency_city = models.DecimalField(
        max_digits=4, decimal_places=1, default=0.0)
    fuel_efficiency_highway = models.DecimalField(
        max_digits=4, decimal_places=1,  default=0)
    horsepower = models.IntegerField(blank=True, default=135)
    key_features = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Team(models.Model):
    Id = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    picture = models.ImageField(upload_to='teams', default=0)
    facebook_link = models.URLField(default="")
    twitter_link = models.URLField(default="")
    instagram_link = models.URLField(default="")
    youtube_link = models.URLField(default="")

    def __str__(self):
        return self.Firstname

    class Meta:
        ordering = ['Id', 'Position']


class Testominals(models.Model):
    Id = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Testominalstext = models.TextField(max_length=500)
    picture = models.ImageField(upload_to='testimonials', default=0)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.Firstname

    class Meta:
        ordering = ['Id', 'Firstname']

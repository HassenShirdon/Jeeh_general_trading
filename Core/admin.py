from django.contrib import admin
from . models import Product, Team, Testominals
# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','Price']



@admin.register(Team)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['Id','Firstname','Lastname','Position']


@admin.register(Testominals)
class TestimonialsModelAdmin(admin.ModelAdmin):
    list_display=['Id', 'Firstname','Lastname' ,'position']




from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class SliderModelAdmin(admin.ModelAdmin):
    list_display =['id','product_name','price','quantity']
from django.db import models
from .MyInventoryApp.models import WaterBottle, Supplier

a = WaterBottle.objects.all()
a = Supplier.objects.all().order_by('country')
a = WaterBottle.objects.all().order_by('brand')
a = WaterBottle.objects.filter(color == 'black')
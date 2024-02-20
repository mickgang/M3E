from django.db import models
from django.utils import timezone

class Supplier(models.Model):
    name = models.CharField(max_length=300, default='default')
    country = models.CharField(max_length=300, default='default')
    city = models.CharField(max_length=300, default='default')
    created_at = models.DateTimeField(blank=True, null=True)

    def getName(self):
        return self.name
    
    def __str__(self):
        strreturn = self.name +" - "+self.city+", "+self.country+" created at: "+str(self.created_at)
        return strreturn


class WaterBottle(models.Model):
    sku = models.CharField(max_length=300, default='default')
    brand = models.CharField(max_length=300, default='default')
    cost = models.DecimalField(max_digits=20,decimal_places=2, default=1)
    size = models.CharField(max_length=300, default='default')
    mouthsize = models.CharField(max_length=300, default='default')
    color = models.CharField(max_length=300, default='default')
    suppliedby = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    currentquant = models.IntegerField(default=1)
    
    def __str__(self):
        strreturn = "{}: {}, {}, {}, {}, supplied by {}, PHP {}: {}".format(self.sku,self.brand,self.mouthsize, self.size, self.color,self.suppliedby,self.cost,self.currentquant)
        return strreturn
# Create your models here.
    
#CHECK FOLLOWING (Not yet Implemented directly)
#Ident of WB by SKU
#One Supplier can many SKU
#One SKU can be supplied by only one supplier
from django.db import models
from datetime import datetime
from realtors.models import Realtor # мэй би придется убрать приписки бтре проджект

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 20)
    description = models.TextField(blank= True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits = 2, decimal_places = 1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to ='photos/%Y/%m/%d/') #интересно, все фотки будут сваливаться от разных лотов в одну папку или же это для каждого отделььного листинга?
    photo_1 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank = True)
    photo_2 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank = True)
    photo_3 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank = True)
    photo_4 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank = True)
    photo_5 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank = True)
    photo_6 = models.ImageField(upload_to ='photos/%Y/%m/%d/', blank = True)
    is_published = models.BooleanField(default=True)
    list_date =  models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title


    """[title: STR
adress: STR
city: STR
state: STR
zipcode: STR
description: TEXT
price: INT
bedrooms: INT
bathrooms: INT
garage: INT [0]
sqft: INT
lot_size: FLOAT
is_published: BOOL [true]
list_date: DATE
photo_main: STR
photo_1:  STR
photo_2:  STR
photo_3:  STR
photo_4:  STR
photo_5:  STR
photo_6:  STR]
    """
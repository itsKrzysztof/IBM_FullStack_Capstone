from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null= False, max_length=30, default='Mazda')
    description = models.CharField(null= False, max_length=300, default='Mazda card are superb')

    def __str__(self):
        return 'Name:' + self.name + ',' + \
            'Description:' + self.description
            
class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    OTHERS = 'others'
    CAR_CHOICES = [(SEDAN, "Sedan"), (SUV, 'SUV'), (WAGON, 'Wagon'), (OTHERS, 'Others')]
    carmake = models.ForeignKey(CarMake, null= True, on_delete=models.CASCADE)
    name = models.CharField(null= False, max_length=30, default='CX-30')
    dealerid = models.IntegerField(null=True)
    cartype = models.CharField(null= False, max_length=20, choices= CAR_CHOICES, default=SEDAN)
    year = models.DateField(null= True)

    def __str__(self):
        return 'Name ' + self.name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

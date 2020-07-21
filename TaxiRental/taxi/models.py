from django.db import models
from django.core.validators import RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField

Destination_choices = ( 
    ("Panbazaar", "Panbazaar"), 
    ("Jalukbari", "Jalukbari"), 
    ("Airport", "Airport"), 
    ("PaltanBazaar", "PaltanBazaar"), 
    ("GS Road", "GS Road"), 
    ("Maligaon", "Maligaon"), 
) 

Car_type_choices = ( 
    ("Maruti Alto", "Maruti Alto"), 
    ("Swift Dzire", "Swift Dzire"), 
    ("Innova", "Innova"), 
    ("Indica", "Indica"), 
    ("Carpool", "Carpool"), 
) 

Distance = {
    'Panbazaar':21,
    'Jalukbari':17,
    'Airport':25,
    'PaltanBazaar':21,
    'GS Road':22,
    'Maligaon':16,
}

Rate_per_km = {
    'Maruti Alto':10,
    'Swift Dzire':15,
    'Innova':20,
    'Indica':15,
    'Carpool': 6,
}

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    
    phone_regex = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')
    
    ono = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10, null=False, validators=[phone_regex])
    destination = models.CharField(max_length=50, choices=Destination_choices, default='Panbazaar')
    car_type = models.CharField(max_length=50, choices=Car_type_choices, default='Maruti Alto')

    def __str__(self):
        return str(self.ono)

    def tot_price(self):
        dist = Distance[self.destination]
        rate = Rate_per_km[self.car_type]
        return dist*rate


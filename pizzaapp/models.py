from django.db import models
#import the user class
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=25)

    def __str__ (self):
        return self.name

class Name(models.Model):
    name = models.CharField(max_length=25)
    type = models.ForeignKey(Type, blank=True, null=True, on_delete=models.CASCADE, related_name="Typename")
    def __str__ (self):
        return self.name

class Toppings(models.Model):
    name =  models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Size(models.Model):
    name =  models.CharField(max_length=25)

    def __str__(self):
        return self.name

#pizza  class
class Item(models.Model):
    type = models.ForeignKey(Type, blank=True, on_delete=models.CASCADE, related_name="Type")
    name = models.ForeignKey(Name, blank=True, on_delete=models.CASCADE, related_name="Name")
    size = models.ForeignKey(Size, blank=True, null=True, on_delete=models.CASCADE, related_name="Size")
    toppings = models.ManyToManyField(Toppings, blank=True, related_name="Toppings")
    extracheese = models.BooleanField(blank=True)
    price = models.IntegerField()


    # usefull string  representations
    def __str__(self):
        # change toppings to string
        toppings = ", ".join(str(seg) for seg in self.toppings.all())
        return f"type:  {self.name} size: {self.size} toppings: {toppings} "


# pizza menu class
class Menu(models.Model):
    type = models.ForeignKey(Type, blank=True, on_delete=models.CASCADE, related_name="Type_menu")
    name = models.ForeignKey(Name, blank=True, on_delete=models.CASCADE, related_name="Name_menu")
    size = models.ForeignKey(Size,  blank=True, null=True, on_delete=models.CASCADE, related_name="Size_menu")
    no_toppings = models.IntegerField(blank=True, null=True)
    baseprice = models.FloatField()

    def __str__(self):
        return f"type:  {self.name} size: {self.size} toppings: {self.no_toppings}"


# shop cart Class
class Shop_cart(models.Model):
    #user object
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    #pizza objects
    items = models.ManyToManyField(Item, blank=True, related_name="ItemsPizza")
    #change to string
    
    def __str__(self):
        return self.user.first_name

# orders Class
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="UserOrder")
    items = models.ManyToManyField(Item, blank=True, related_name="items")
    def __str__(self):
        return self.user.first_name




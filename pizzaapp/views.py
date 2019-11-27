#libaries for login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#http
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from .models import *

from django.forms.models import model_to_dict
import json
from django.core import serializers
import sys
sys.setrecursionlimit(1500)

#adapted usercreationform
from pizzaapp.forms import SignUpForm

def orders(request):
    #check if logged in 
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
  

    context = {"orders": Order.objects.all(),
                "items": Item.objects.all()
            }
                    
    return render(request, "orders.html", context)

def product(request, type, name, size):
    if request.method == 'GET':
        try: 
            nameh = Name.objects.get(name=name)
            typeh = Type.objects.get(name=type)

            if size == 'None':
                product = Menu.objects.filter(type=typeh, name=nameh).first()

            else:
                sizeh = Size.objects.get(name=size)
                product = Menu.objects.filter(type=typeh, name=nameh, size=sizeh).first()
            
            print(str(type))
        except Menu.DoesNotExist:
            raise Http404("product not available")

        context = { "Types": Type.objects.all(),
            "Product": product,
            "Items": Menu.objects.all(),
            "Names": Name.objects.all(),
            "Sizes": Size.objects.all(),
            "Toppings": Toppings.objects.all(),
            }
        return render(request, "product.html", context)

    if request.method == 'POST':
        
        #retrieve data 
        type = Type.objects.get(name=request.POST["type"])
        name = Name.objects.get(name=request.POST["name"])
        if not request.POST.get("size"):
            size = None
        else:
            size = Size.objects.get(name=request.POST["size"])
        extracheese = request.POST.get("extracheese", False)
        amount = int(request.POST.get("amount"))
        print(amount)
        # topping as a list
        toppings = request.POST.getlist("toppings")
        
        # new item object
        item = Item()
        
        #item.type = Type.objects.get(name=base)
        item.size = size
        item.type = type
        item.name = name

        # if pizza add number of toppings for pricecheck, otherwise not
        if type.name == "Pizza":
            pricecheck = Menu.objects.get(size=size, type=type, name=name, no_toppings=len(toppings))
        
            item.price = pricecheck.baseprice
            
        else:
            pricecheck = Menu.objects.get(size=size, type=type, name=name)
            item.price = pricecheck.baseprice
            item.price += len(toppings) * 0.5
        #item.price += pricecheck.price
        # now add the cheese
        if extracheese:
            item.price += 0.5
            item.extracheese = True

        print(item.price)
        #pizza.price = pricecheck.price 
    # plus message
        #backend price check
        #################### use try exept to catch up otherbugs
        #first save to add toppings
        item.price = item.price * amount ################################
        print(item.price)
        item.save()
        for topping in toppings:
            item.toppings.add(Toppings.objects.get(name=topping))
        # save again
        item.save()

        # add pizza object to users shop cart

        #get users shop cart  + !!!!error handling!!!
        shop_cart = Shop_cart.objects.get(user=request.user)
        
        #add the pizza items to shoppingcart
        shop_cart.items.add(item)
        shop_cart.totalprice += item.price
        print(shop_cart.totalprice)
        shop_cart.save()
        
        return HttpResponseRedirect(reverse("shoppingcart"))
         
# function name to be found in urls.py, 
#httpresponseredirect(reverse) is a way to redirect to another adres
# render(template) to render
        
def shoppingcart(request):

    #check if logged in 
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
        
    # load cart page
    if request.method == 'GET':
        cart = Shop_cart.objects.get(user=request.user)
        #items = []
        #for seg in cart.items_pizza.all():
            #items.append(seg)
        #context = {"items": items}

        # calculate total price
        #totalprice = 0
        #for item in cart.items:
        
        context2 = {"items": cart.items.all(),
                    "cart": cart}
        return render(request, "shoppingcart.html", context2)
    # place order and delete content

    if request.method == 'POST':

        #get cart object
        cart = Shop_cart.objects.get(user=request.user)

        if 'order' in request.POST:
        #create new order object
            order = Order()
        # add cart and user data to order and save 
            order.user = request.user
            order.totalprice = cart.totalprice
            order.save()

        # add order to items
        for item in cart.items.all():

            # if user removed a item
            if str(item) in request.POST:
                
                item.delete()
                # decrease amount
                cart.totalprice -= item.price
                cart.save()
            
            # if user presses the place order buttom
            if 'order' in request.POST:
                print("add to order")
                item.order = order
                cart.items.remove(item)
                cart.totalprice = 0
                cart.save()
                item.save()

        return HttpResponseRedirect(reverse("shoppingcart"))

def index(request):

    #check if logged in 
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    # variables to give to the html
    context = { "Types": Type.objects.all(),
                "Items": Menu.objects.all(),
                "Names": Name.objects.all(),
                "Sizes": Size.objects.all(),
                "Toppings": Toppings.objects.all()}
    
    if request.method == 'GET':
        return render(request, "index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

def register_view(request):
    # post method
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form) #####
        #check if  form is valid
        if form.is_valid():
            form.save()
            #authenticate user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            # create a shop cart upon register
            shop_cart = Shop_cart()
            shop_cart.user = user
            shop_cart.save()

            # create a orders table upon register
            #orders = Orders()
            #orders.user = user
            #orders.save()

            return HttpResponseRedirect(reverse("index"))
    
    # getmethod
    else:
        form = SignUpForm()
    return render(request, "register.html", {'form': form})

def failure(request):
    return render(request, "failure.html")
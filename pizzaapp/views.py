#libaries for login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#http
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render
from .models import *

#adapted usercreationform
from pizzaapp.forms import SignUpForm

# handles order page
def orders(request):
    #check if logged in as admin 
    if not request.user.is_authenticated or not request.user.is_superuser:
        return render(request, "login.html", {"message": None})
    

    context = {"orders": Order.objects.all(),
                "items": Item.objects.all()
            }
                    
    return render(request, "orders.html", context)

# handles product page
def product(request, type, name, size):

    #check if logged in 
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})

    if request.method == 'GET':
        try: 
            nameh = Name.objects.get(name=name)
            typeh = Type.objects.get(name=type)

            if size == 'None':
                product = Menu.objects.filter(type=typeh, name=nameh).first()

            else:
                sizeh = Size.objects.get(name=size)
                product = Menu.objects.filter(type=typeh, name=nameh, size=sizeh).first()
            
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
        size = Size.objects.filter(name=request.POST["size"]).first()
        extracheese = request.POST.get("extracheese", False)
        amount = int(request.POST.get("amount"))
 
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

       
        # add extra cheese
        if extracheese:
            item.price += 0.5
            item.extracheese = True
     
        #backend price check
        item.price = item.price * amount ################################
        item.amount = amount

        # round 2 decimals
        item.price =  round(item.price, 2)
        item.save()

        # add toppings to item
        for topping in toppings:
            item.toppings.add(Toppings.objects.get(name=topping))
        # save again
        item.save()


        # get users shop cart 
        shop_cart = Shop_cart.objects.get(user=request.user)
        
        #add the pizza items to shoppingcart, calculate total price of shopcart and save
        shop_cart.items.add(item)
        shop_cart.totalprice += item.price
        shop_cart.totalprice = round(shop_cart.totalprice, 2)
        shop_cart.save()
        
        # return same page
        return HttpResponseRedirect(reverse("shoppingcart"))
         
# handles shoppingcart page        
def shoppingcart(request):

    #check if logged in 
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
        
    # load cart page
    if request.method == 'GET':
        cart = Shop_cart.objects.get(user=request.user)

        context2 = {"items": cart.items.all(),
                    "cart": cart}
        return render(request, "shoppingcart.html", context2)

    # change to cart 
    if request.method == 'POST':

        # get cart object
        cart = Shop_cart.objects.get(user=request.user)
        
        # if order is made
        if 'order' in request.POST and cart.items != None:
        #create new order object
            order = Order()
        # add cart and user data to order and save 
            order.user = request.user
            order.totalprice = round(cart.totalprice, 2)
            order.save()

        # add order to items
        for item in cart.items.all():

            # if user removed a item
            if str(item) in request.POST:
                item.delete()
                cart.totalprice -= item.price
                cart.save()
                break
            
            # if user presses the place order buttom
            if 'order' in request.POST and cart.items != None:
                item.order = order
                cart.items.remove(item)
                cart.totalprice = 0
                cart.save()
                item.save()
                return HttpResponseRedirect(reverse("orderplaced"))

        return HttpResponseRedirect(reverse("shoppingcart"))

# handles menu page
def index(request):

    #check if logged in 
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})

    # variables to give to the html page
    context = { "Types": Type.objects.all(),
                "Items": Menu.objects.all(),
                "Names": Name.objects.all(),
                "Sizes": Size.objects.all(),
                "Toppings": Toppings.objects.all()}
    
    if request.method == 'GET':
        return render(request, "index.html", context)

# handles login 
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

# handles logout
def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

def register_view(request):
    #check if logged in 
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
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
            shop_cart.totalprice = 0
            shop_cart.save()

            return HttpResponseRedirect(reverse("index"))
    
    # getmethod
    else:
        form = SignUpForm()
    return render(request, "register.html", {'form': form})

def failure(request):
    return render(request, "failure.html")

def orderplaced(request):
    return render(request, "orderplaced.html")
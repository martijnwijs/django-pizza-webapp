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

def orders(request):
    #check if logged in 
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})


    context2 = {"items": Order.objects.all()}
    return render(request, "orders.html", context2)

def product(request, type, name, size):
    if request.method == 'GET':
        try: 
            nameh = Name.objects.get(name=type)
            typeh = Type.objects.get(name=name)
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
        size = Size.objects.get(name=request.POST["size"])
        extracheese = request.POST.get("extracheese", False)
        
        # topping as a list
        toppings = request.POST.getlist("toppings")

       
         
        
        # new item object
        item = Item()
        #item.type = Type.objects.get(name=base)
        item.size = size
        
        # if pizza add no of toppings for pricecheck, otherwise not
        if type.name == "Pizza":
            pricecheck = Menu.objects.get(size=size, type=type, no_toppings=len(toppings))
            item.price = 0
        else:
            pricecheck = Menu.objects.get(size=size, type=type)
            item.price = len(toppings) * 0,5
        item.price += pricecheck.price
        # now add the cheese
        if extracheese:
            item.price += 0,5

        
        #pizza.price = pricecheck.price 
    # plus message
        #backend price check
        #################### use try exept to catch up otherbugs
        #first save to add toppings
        item.save()
        for topping in toppings:
            item.toppings.add(Toppings.objects.get(name=topping))
        # save again
        item.save()

        # add pizza object to users shop cart

        #get users shop cart  + !!!!error handling!!!
        shop_cart = Shop_cart.objects.get(user=request.user)
        
        #add the pizza items
        shop_cart.items.add(item)
        shop_cart.save()
        
        return HttpResponseRedirect(reverse("failure"))
         
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
        context2 = {"items": cart.items.all()}
        return render(request, "shoppingcart.html", context2)
    # place order and delete content
    if request.method == 'POST':

        #get cart object
        cart = Shop_cart.objects.get(user=request.user)

        if 'order' in request.POST:
        #create new order object
            order = Order()
        # add cart to order and save order
            order.user = request.user
            order.save()

        # add items to order and delete them from cart
        for seg in cart.items_pizza.all():

            # if user removed a item
            if str(seg) in request.POST:
                print("seg")
                seg.delete()
                cart.save()
            
            # if user presses the place order buttom
            if 'order' in request.POST:
                print("add to  order")
                order.items.add(seg)
                seg.delete()
                order.save()
                cart.save()

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
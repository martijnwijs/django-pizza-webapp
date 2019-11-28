from django.urls import path


from . import views

# first element webadres, second element function in views, third element name to be  reference by httpresponse
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("failure", views.failure, name = "failure"),
    path("shoppingcart", views.shoppingcart, name = "shoppingcart"),
    path("orders", views.orders, name = "orders"),
    path("<str:type>/<str:name>/<str:size>", views.product, name="product"),
    path("orderplaced", views.orderplaced, name="orderplaced")
    ]
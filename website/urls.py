from django.contrib import admin
from django.urls import path
from website import views


urlpatterns = [
    path("", views.index, name='website'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("index2", views.index2, name='index2'),
    path("products", views.products, name='products'),
    path("login_page", views.login_page, name='login_page'),
    path("logout_page", views.logout_page, name='logout_page'),
    path("signup", views.signup, name='signup'),
    path("camera", views.camera, name='camera'),
    path("mouse", views.mouse, name='mouse'),
    path("speaker", views.speaker, name='speaker'),
    path("laptop/<int:myid>", views.laptop, name='laptop'),
    path("iphone", views.iphone, name='iphone'),
    path("contactus", views.contactus, name='contactus'),
    path("smartWatch", views.smartWatch, name='smartWatch'),
    path("headphone", views.headphone, name='headphone'),
    path("charger", views.charger, name='charger'),
    path("checkout", views.checkout, name='checkout'),
    path("thankyou", views.thankyou, name='thankyou'),
    path("placeorder", views.placeorder, name='placeorder'),
    # cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart_detail', views.cart_detail, name='cart_detail'),
    # path('laptop/cart_detail', views.cart_detail, name='cart_detail'),
]

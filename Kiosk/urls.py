from django.urls import path
from . import views

urlpatterns = [
    path('grabgrub', views.main, name='main'),
    path('grabgrub/viewcustomers.html', views.customers, name='customers'),
    path('grabgrub/addcustomers.html', views.add_customer, name='addcustomer'),
    path('grabgrub/editcustomer/<int:pk>/', views.edit_customer, name='editcustomer'),
    path('grabgrub/viewcustomerorders/<int:pk>/', views.view_customer_orders, name='viewcustomerorders'),

    path('grabgrub/viewfood.html', views.food, name='food'),
    path('grabgrub/addfood.html', views.add_food, name='addfood'),
    path('grabgrub/editfood/<int:pk>/', views.edit_food, name='editfood'),

    path('vieworder.html', views.order, name='order'),
    path('grabgrub/order.html', views.add_order, name='addorder'),
    path('grabgrub/editorder/<int:pk>/', views.edit_order, name='editorder'),
    path('grabgrub/deleteorder/<int:pk>/', views.delete_order, name='deleteorder'),
]

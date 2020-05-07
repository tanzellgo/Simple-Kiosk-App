from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Customer, Food, Order, OrderLine

def main(request):
    return render(request, "Kiosk/main.html")

def customers(request):
    customer_objects = Customer.objects.all()   
    return render(request, 'Kiosk/viewcustomers.html', {'customer':customer_objects})

def add_customer(request):
    if(request.method=="POST"):
        custname = request.POST.get('cname')
        custcity = request.POST.get('ccity')
        custadd = request.POST.get('cadd')
        Customer.objects.create(name=custname, city=custcity, address=custadd)
        return redirect('customers')
    else:
        return render(request, 'Kiosk/addcustomers.html')

def edit_customer(request, pk):
    if(request.method=="POST"):
        custname = request.POST.get('cname')
        custcity = request.POST.get('ccity')
        custadd = request.POST.get('cadd')
        Customer.objects.filter(pk=pk).update(name=custname, city=custcity, address=custadd)
        return redirect('customers')
    else:
        c = get_object_or_404(Customer, pk=pk)
        return render(request, 'Kiosk/editcustomer.html', {'c':c})

def view_customer_orders(request, pk):
        c = Customer.objects.filter(pk=pk)
        order_objects = Order.objects.filter(cust_order__in=c)
        orderline_objects = OrderLine.objects.filter(ord__in=order_objects)
        total_order = OrderLine.objects.filter(ord__in=order_objects).aggregate(sum=Sum('total'))['sum']
        return render(request, 'Kiosk/viewcustomerorder.html', {'c':c, 'order':order_objects, 'orderline':orderline_objects, 'sum':total_order})


def food(request):
    food_objects = Food.objects.all()
    return render(request, 'Kiosk/viewfood.html', {'food':food_objects})

def add_food(request):
    if(request.method=="POST"):
        food_name = request.POST.get('fname')
        food_description= request.POST.get('fdescription')
        food_price = request.POST.get('fprice')
        Food.objects.create(name=food_name, description=food_description, price=food_price)
        return redirect('food')
    else:
        return render(request, 'Kiosk/addfood.html')

def edit_food(request, pk):
    if(request.method=="POST"):
        food_name = request.POST.get('fname')
        food_description = request.POST.get('fdescription')
        food_price = request.POST.get('fprice')
        Food.objects.filter(pk=pk).update(name=food_name, description=food_description, price=food_price)
        return redirect('food')
    else:
        f = get_object_or_404(Food, pk=pk)
        return render(request, 'Kiosk/editfood.html', {'f':f})

def order(request):
    order_objects = Order.objects.all()
    orderline_objects = OrderLine.objects.all()
    return render(request, 'Kiosk/vieworder.html', {'order':order_objects, 'orderline':orderline_objects})

def add_order(request):
    customer_objects = Customer.objects.all()
    food_objects = Food.objects.all()
    order_f_name = None
    if(request.method=="POST"):
        order_c_name = request.POST.get('ocname')
        order_f_name = request.POST.get('forder')
        order_payment = request.POST.get('payment')
        order_quantity = request.POST.get('quantity')
        order_total = float(order_quantity) * Food.objects.get(pk=order_f_name).price
        o = Order.objects.create(cust_order=Customer.objects.get(pk=order_c_name), mode_payment=order_payment)
        OrderLine.objects.create(ord=Order.objects.get(pk=o.pk), food=Food.objects.get(pk=order_f_name), quantity=order_quantity, total=order_total)
        return redirect('order')
    else:
        return render(request, 'Kiosk/addorder.html', {'customer':customer_objects, 'food':food_objects})

def edit_order(request, pk):
    if(request.method=="POST"):
        order_c_name = request.POST.get('ocname')
        order_f_name = request.POST.get('forder')
        order_payment = request.POST.get('payment')
        order_quantity = request.POST.get('quantity')
        order_total = float(order_quantity) * Food.objects.get(pk=order_f_name).price
        o = Order.objects.update(cust_order=Customer.objects.get(pk=order_c_name), mode_payment=order_payment)
        OrderLine.objects.update(ord=Order.objects.get(pk=o.pk), food=Food.objects.get(pk=order_f_name), quantity=order_quantity, total=order_total)
        return redirect('order')
    else:
        o = get_object_or_404(Order, pk=pk)
        ol = get_object_or_404(OrderLine, ord=o)
        return render(request, 'Kiosk/editorder.html', {'o':o, 'ol':ol})

def delete_order(request, pk):
    Order.objects.filter(pk=pk).delete()
    OrderLine.objects.filter(pk=pk).delete()
    return redirect('order')
# Create your views here.

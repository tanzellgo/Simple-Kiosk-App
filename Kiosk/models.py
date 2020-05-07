from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def getName(self):
        return(self.name)

    def getDesc(self):
        return(self.description)

    def getPrice(self):
        return(self.price)

    def __str__(self):
        return f"{self.pk}: {self.name} - {self.price}, {self.description} created at: {self.created_at}"

class Customer(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    objects = models.Manager()

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def __str__(self):
        return f"{self.pk}: {self.name} - {self.address}, {self.city}"

class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    payment = [
        ('Cash', 'Cash'),
        ('Card', 'Card')
    ]
    mode_payment = models.CharField(max_length=4, choices=payment)
    cust_order =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    objects = models.Manager()

    def getMode(self):
        return self.mode_payment 

    def __str__(self):     
        return f"{self.pk}: {self.cust_order.name}, {self.cust_order.address}, {self.cust_order.city}, {self.mode_payment}, ordered at {self.ordered_at}"

class OrderLine(models.Model):
    ord = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.FloatField()
    total = models.FloatField()
    objects = models.Manager()

    def getQuantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.pk}: {self.ord.pk} - {self.food.name}, {self.quantity}, {self.total}"


# Create your models here.

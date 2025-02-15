from django.db import models

class Service(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    details = models.TextField()
    image1 = models.ImageField(upload_to='service_images/')
    image2 = models.ImageField(upload_to='service_images/')
    image3 = models.ImageField(upload_to='service_images/')

class Order(models.Model):
    uname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    service_id = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    phno = models.CharField(max_length=20)
    email = models.EmailField()
    pay_method = models.CharField(max_length=100)
    add1 = models.CharField(max_length=255)
    add2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    qty = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    placed_on = models.DateTimeField(auto_now_add=True)

class Com_Order(models.Model):
    uname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    service_id = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    phno = models.CharField(max_length=20)
    email = models.EmailField()
    add1 = models.CharField(max_length=255)
    add2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    completed_on = models.DateTimeField(auto_now_add=True)
    placed_on = models.DateTimeField()
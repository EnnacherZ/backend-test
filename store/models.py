from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


shoe_choices= [
    ('Mocassin', 'Mocassin'),
    ('Basket', 'Basket'),
    ('Medical', 'Medical'),
    ('Classic', 'Classic'),
]


class Shoe(models.Model):
    productType = models.CharField(default='Shoe', max_length=20, editable=False)
    category = models.CharField(max_length=100, choices=shoe_choices)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    newest = models.BooleanField(default=False) 
    promo = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0)
    image = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    image1 = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    image2 = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    image3 = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    image4 = models.ImageField(upload_to='shoes/', default='shoes/empty.jpg')
    def __str__(self):
        return "%s %s %s"%(self.category, self.ref, self.name)

class ShoeDetail(models.Model):
    productId = models.ForeignKey(Shoe,on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s %s"%(self.productId, "size : " + str(self.size) , "quantity : "+str(self.quantity))

class Sandal(models.Model):
    productType = models.CharField(default='Sandal', max_length=20, editable=False)
    category = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    newest = models.BooleanField(default=False) 
    promo = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0)
    image = models.ImageField(upload_to='sandals/')
    def __str__(self):
        return "%s %s %s"%(self.category, self.ref, self.name)

class SandalDetail(models.Model):
    productId = models.ForeignKey(Sandal, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s %s"%(self.productId, self.size, self.quantity)
    
class Shirt(models.Model):
    productType = models.CharField(default='Shirt', max_length=20, editable=False)
    category = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    newest = models.BooleanField(default=False) 
    promo = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0)
    image = models.ImageField(upload_to='Shirts/')
    def __str__(self):
        return "%s %s %s"%(self.category, self.ref, self.name)
    
class ShirtDetail(models.Model):
    productId = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    size = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s %s"%(self.productId, self.size, self.quantity)

class  Pant(models.Model):
    productType = models.CharField(default='Pant', max_length=20, editable=False)
    category = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    newest = models.BooleanField(default=False) 
    promo = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], default=0)
    image = models.ImageField(upload_to='Shirts/')
    def __str__(self):
        return "%s %s %s"%(self.category, self.ref, self.name)
    
class PantDetail(models.Model):
    productId = models.ForeignKey(Pant, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return "%s %s %s"%(self.productId, self.size, self.quantity)

class Client(models.Model):
    order_id = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s %s"%(self.first_name, self.last_name, self.order_id)


class ProductOrdered(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField(editable=False)
    product_type = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    ref = models.CharField(max_length=50)
    name = models.CharField(max_length=50)



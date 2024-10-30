from django.db import models
from account_app.models import Account

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category_image = models.ImageField(upload_to='category_images/',null=True,blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/',null=True,blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, related_name='stocks', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'


class Order(models.Model):
    customer = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='customer_order')
    total_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    payment_method = models.CharField(max_length=50, default='Cash On Delivery')
    order_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Order #{self.pk} - {str(self.order_time)}"
    
    class Meta:
        ordering = ('-id',)



class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    order_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.product.name
    
    class Meta:
        ordering = ('-id',)
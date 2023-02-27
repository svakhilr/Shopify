from django.db import models
from account.models import Account,Address
from store.models import Product,Variation

class Order(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    order_number = models.CharField(max_length=100, null=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL,null=True)
    payment_method = models.CharField(max_length=30,blank=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    order_status =(
          ('Processing','Processing'),
          ('Confirmed','Confirmed'),
          ('Out For Shipping', 'Out For Shipping'),
          ('Delivered', 'Delivered'),
          ('Cancel', 'Cancel'),
    )
    status =models.CharField(max_length=100,choices=order_status,default='Processing')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    user= models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)
    
    def total(self):
        return self.quantity*self.product.price
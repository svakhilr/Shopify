from django.db import models
from store.models import Product,Variation
from account.models import Account

class Cartitem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="cart_item")
    user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='cart_user')
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def get_total(self):
        return self.product.price*self.quantity
    
    def __str__(self):
        return str(self.product)
    

class Coupon(models.Model):
    coupon_code= models.CharField(max_length=100)
    coupon_limit= models.IntegerField(default=1)
    discount_amt= models.IntegerField()
    minimum_amt = models.IntegerField()
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return self.coupon_code

    

class ReviewCoupon(models.Model):
    coupon = models.ForeignKey(Coupon,on_delete=models.CASCADE,related_name='coupon')
    user =  models.ForeignKey(Account,on_delete=models.CASCADE,related_name='coupon_user')


    def __str__(self):
        return str(self.user.first_name)


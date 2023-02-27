from django.contrib import admin
from cart.models import Cartitem,Coupon,ReviewCoupon

admin.site.register(Cartitem)
admin.site.register(Coupon)
admin.site.register(ReviewCoupon)

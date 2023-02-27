from django.urls import path,include
from . import views

urlpatterns = [
    path('addtocart/', views.addtocart , name='addtocart'),
    path('viewcart/' , views.cart, name='cart-view'),
    path('updatecart/',views.update_cart,name='updatecart'),
    path('removeitem/<int:id>/',views.removeitem,name='removeitem'),
    path('applycoupon/',views.apply_coupon,name='applycoupon')

    

]
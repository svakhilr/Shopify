from django.urls import path
from .import views


urlpatterns = [
    path('checkout/', views.checkout , name='checkout'),
    path('placeorder/',views.order,name='order'),
    path('cod/<int:id>/',views.COD,name='cod'),
    path('invoice/', views.thankyou, name='invoice'),
    path('paypalpayment/',views.paypal,name='paypalpayment'),
    
    
    

]
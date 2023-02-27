from django.urls import path
from .import views
urlpatterns = [
    
    path('viewstore/',views.storepage, name="store-page"),
    path('category<slug:category_slug>/<slug:product_slug>/',views.productdetail, name="product-detail")
    

]
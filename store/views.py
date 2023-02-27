from django.shortcuts import render
from store.models import Product

def storepage(request):
    products= Product.objects.all()
    context={"products":products}
    return render(request,"store/store.html",context)


def productdetail(request,category_slug,product_slug):
    product= Product.objects.get(category__slug=category_slug,slug=product_slug)
    print(product)
    context={
        "product":product
    }
    return render(request,'store/productdetail.html',context)

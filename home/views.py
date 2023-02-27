from django.shortcuts import render
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def home(request):
    products= Product.objects.filter(is_available=True)
    context={"products":products}
    return render(request, 'home/home.html',context)


def quick_view(request):
    id= request.GET.get('prod_id')
    product = Product.objects.get(id=id)
    print(type(product))
    print(type(product.product_name))
    image1= product.images.url
    image2 = product.images1.url
    image3 = product.images2.url
    print(image1)
    print(image3)
    response={'product_name':product.product_name,
              'product_price':product.price,
              'image1':image1,
              'image2':image2,
              'image3':image3}
    

    return JsonResponse(response)


def errorpage(request):
    return render(request,'home/errorpage.html')

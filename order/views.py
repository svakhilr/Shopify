from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cartitem,ReviewCoupon,Coupon
from .models import Order,OrderItem
from account.models import Address
from store.models import Product
import datetime
from django.http import JsonResponse
import random
from django.contrib import messages

# Create your views here.


@login_required(login_url='login')
def checkout(request):
    user=request.user
    cartitems=Cartitem.objects.filter(user=user)
    if "discount" in request.session:
        discount = request.session["discount"]
    else:
        discount=0
    
    print(discount)
    
    total=0
    for item in cartitems:
        total+=item.get_total()

    tax= round(0.01*total,2)
    grand_total= tax+total

    grand_total-=discount
    request.session['grand_total']= grand_total
    print(request.session['grand_total'])
    context={"cartitems":cartitems,
             'total':total,
             "grand_total":grand_total,
             "discount":discount,
             "tax":tax}
    return render(request,'order/checkout.html',context)


def order(request):
    if request.method == "POST":
        user= request.user
        address = Address()
        address.first_name = request.POST.get('first_name')
        address.last_name = request.POST.get('last_name')
        address.phone_number = request.POST.get('phone')
        address.address1 = request.POST.get('address_line_1')
        address.address2 = request.POST.get('address_line_2')
        address.city = request.POST.get('city')
        address.state = request.POST.get('state')
        address.country = request.POST.get('country')
        address.user=user
        address.save()
        
        grand_total= request.session['grand_total']
        print(grand_total)
        if "discount" in request.session:
            discount= request.session['discount']
        else:
            discount=0    
        
        print(grand_total)
        
        ordered= Order()
        ordered.user = user
        ordered.address= address
        ordered.grand_total=grand_total
        yr = int(datetime.date.today().strftime('%Y'))
        dt = int(datetime.date.today().strftime('%d'))
        mt = int(datetime.date.today().strftime('%m'))
        d = datetime.date(yr,mt,dt)
        current_date = d.strftime("%Y%m%d") #20210305
        order_no = str(random.randint(1111111111,9999999999))

        order_number = current_date + str(user.id)+ order_no
        ordered.order_number = order_number
        ordered.save()
        print(ordered.grand_total)
        total=0

        cartitems= Cartitem.objects.filter(user=user)

        for item in cartitems:
            total += item.get_total()

        tax= round(total*0.01,2)
        
        context = {
            'order':ordered,
            'cartitems':cartitems,
            'discount':discount,
            'total':total,
            'tax':tax
        }

        return render(request, 'order/payment.html', context)
    
    return redirect('/')


def COD(request,id):
    order= Order.objects.get(id=id)
    cartitems = Cartitem.objects.filter(user=request.user)
    order.payment_method="COD"
    order.save()

    for cartitem in cartitems:
        product = Product.objects.get(id =cartitem.product_id )
        product.stock-= cartitem.quantity
        product.save()
        orderitem=OrderItem()
        orderitem.user = request.user
        orderitem.product = cartitem.product
        orderitem.variation = cartitem.variation
        orderitem.quantity = cartitem.quantity
        orderitem.order = order
        orderitem.save()

    cartitems.delete()
    messages.success(request, "Successfully Placed Order")

    return redirect('invoice')

def paypal(request):
    if request.method == 'POST':
        print(request.user)
        order_id = request.POST.get('order')
        transaction_id =request.POST.get('transaction_id')
        order = Order.objects.get(id= order_id)
        cartitems = Cartitem.objects.filter(user=request.user)
        order.payment_method="PAYPAL"
        order.transaction_id=transaction_id
        order.save()
        for cartitem in cartitems:
            orderitem=OrderItem()
            orderitem.user = request.user
            orderitem.product = cartitem.product
            orderitem.variation = cartitem.variation
            orderitem.quantity = cartitem.quantity
            orderitem.order = order
            orderitem.save()

        cartitems.delete()

        return JsonResponse({'status': 'Your order has been placed successfully'})
    return JsonResponse({'message':"INVALID TYPE OF REQUEST"})



def thankyou(request):
    user = request.user
    order = Order.objects.filter(user=user).last()
    if "discount" in request.session:
        discount= request.session['discount']
        del request.session["discount"]
    else:
        discount=0
    total=0
    if "coupon_code" in request.session:
        coupon_code = request.session["coupon_code"]
        coupon = Coupon.objects.get(coupon_code=coupon_code)
        print(coupon)
        review_coupon= ReviewCoupon()
        review_coupon.user=user
        review_coupon.coupon = coupon
        review_coupon.save()
        del request.session["coupon_code"]
    
    if 'grand_total' in request.session:
        del request.session["grand_total"]

    for item in order.order_items.all():
        total += item.total()
    print(total)

    tax= round(total*0.01,2)    
    context={
        'order':order,
        'user':user,
        'discount':discount,
        'total':total,
        'tax':tax
    }
    return render(request,'order/invoice.html',context)


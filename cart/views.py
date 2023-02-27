from django.shortcuts import render,redirect
from store.models import Product,Variation
from .models import Cartitem,Coupon,ReviewCoupon
from django.http import JsonResponse
from django.contrib import messages,auth

def addtocart(request):
    if request.method == 'POST':
        print(request.user)
        
        
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('prod_id'))
            print(request.POST.get('var_id'))
            if not request.POST.get('var_id'):
                flag=4
                return JsonResponse({"flag":flag})
            var_id = int(request.POST.get('var_id'))
            product= Product.objects.get(id=prod_id)
            variation= Variation.objects.get(id=var_id)
            print(prod_id)
            
            if Cartitem.objects.filter(user=request.user,product_id=prod_id,variation_id=var_id).exists():
                flag=1
                
            
            else:
                quantity=1
                Cartitem.objects.create(user=request.user,product=product,variation=variation,quantity=quantity)
                flag=2
            
        else:
            flag=3

        context={"flag":flag}
        return JsonResponse(context)
    


def cart(request):
    if request.user.is_authenticated:
        if "coupon_code" in request.session:
            del request.session["coupon_code"]
            
            del request.session["discount"]
        
        total=0
        user= request.user
        cartitems = Cartitem.objects.filter(user=user)
        for item in cartitems:
            total+=item.get_total()
        if "discount" in request.session:
            discount = request.session["discount"]
        else:
            discount=0

        coupons= Coupon.objects.all()
        
        tax= round(total*0.01,2)
        grand_total= (tax+total)-discount
        request.session['grand_total']=grand_total
        print(grand_total)
        context={"cartitems":cartitems,
                 'total':total,
                 'tax':tax,
                 'discount':discount,
                 'grand_total':grand_total,
                 'coupons':coupons}
        return render(request,'cart/cart.html',context)
    
    else:
        messages.error(request,'Please login')
        return redirect('home')
    

def update_cart(request):
    if request.method == 'POST':
        if "coupon_code" in request.session:
            del request.session["coupon_code"]
            
            del request.session["discount"]
        del request.session["grand_total"]
        cartitem_id = int(request.POST.get('prod_id')) 
        user=request.user
        quantity= int(request.POST.get('quantity'))
        action= request.POST.get('action')
        print(quantity)
        tax=0
        if action == 'add':
            quantity+=1
            cartitem= Cartitem.objects.get(id=cartitem_id,user=user)
            cartitem.quantity=quantity
            cartitem.save()
            cartitems= Cartitem.objects.filter(user=user)
            total=0

            for i in cartitems:
                total+=i.get_total()
            itemtotal=cartitem.get_total()
            print(itemtotal)

        elif action == 'sub':
            quantity-=1
            cartitem= Cartitem.objects.get(id=cartitem_id,user=user)
            cartitem.quantity=quantity
            cartitem.save()
            cartitems= Cartitem.objects.filter(user=user)
            total=0

            for i in cartitems:
                total+=i.get_total()
            
            itemtotal= cartitem.get_total()
            print(itemtotal)

        if "discount" in request.session:
            discount = request.session["discount"]
        else:
            discount=0
        
            
        print(total)
        
        tax= round(0.01*total,2)
        grand_total= tax+total
        grand_total-=discount
        request.session['grand_total']=grand_total
        

        response={'itemtotal':itemtotal,
                  'total':total,
                  'cartitem_id': cartitem_id,
                  'tax':tax,
                  'grand_total':grand_total,
                  'discount':discount,
                  }
        


    
    return JsonResponse(response)


def removeitem(request,id):
    user=request.user
    cartitem = Cartitem.objects.get(id=id,user=user)
    cartitem.delete()
    return redirect('cart-view')
    

def apply_coupon(request):
    if "coupon_code" in request.session:
        del request.session["coupon_code"]
        
        del request.session["discount"]
    del request.session["grand_total"]
    flag=0
    discount=0

    coupon_code= request.POST.get('coupon_code')
    grand_total = float(request.POST.get('grand_total'))

    if Coupon.objects.filter(coupon_code=coupon_code, coupon_limit__gte=1).exists():
        coupon = Coupon.objects.get(coupon_code=coupon_code)
        if not ReviewCoupon.objects.filter(user=request.user,coupon=coupon):
            if coupon.minimum_amt< grand_total:
                discount = coupon.discount_amt
                grand_total -=discount
                flag=2
                request.session["coupon_code"] = coupon_code
                request.session["discount"] = discount 
                request.session["grand_total"]= grand_total

        
        else:
            flag = 1
    
    request.session["grand_total"]=grand_total
    response = {'flag':flag,
                'grand_total':grand_total,
                'discount':discount}
    
    return JsonResponse(response)





    
    
            


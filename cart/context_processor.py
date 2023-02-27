from .models import Cartitem

def cart_count(request):
    item_count=0

    if request.user.is_authenticated:
        items=Cartitem.objects.filter(user=request.user)
        for item in items:
            item_count+=1

    return {"item_count":item_count}
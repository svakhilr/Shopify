from django.shortcuts import render,redirect
from .forms import Registrationform
from .models import Account
from django.contrib import messages,auth




# Create your views here.


def signup(request):
    form=Registrationform()

    if request.method== 'POST':
        form=Registrationform(request.POST)
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password= form.cleaned_data['password']
            
            user= Account.objects.create_user(first_name=first_name,last_name=last_name,password=password,email=email,phone_number=phone_number)
            user.is_active= True
            user.save()
            messages.success(request,'Your account is successfully created')
            return redirect('home')

        else:
            messages.error(request,'oops! please provide proper details')

    else:
        pass
    
    return render(request, 'home/usersignup.html',{'form':form})


def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email,password=password)

        if user:
            auth.login(request, user)
            messages.success(request, "Authenticated Successfully.")
            return redirect('home')

        else:
            messages.error(request,"Wrong Credentials")

    
    return render(request,"home/login.html")


def logout(request):
    auth.logout(request)
    messages.success(request,'Successfully Loged Out')
    return redirect('login')



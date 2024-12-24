from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from Services.models import Service, Order
from django.core.mail import send_mail

# Create your views here.
def home(request):
    services = Service.objects.all()
    qty = request.POST.get('qty')
    return render(request, 'index.html',{'services':services})

def about(request):
    return render(request,'about.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=name).exists():
            messages.error(request,'Username already exists.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists.')
            return redirect('register')
        if pass1 == pass2:
            myuser = User.objects.create_user(name, email, pass1)
            myuser.save()    
            messages.success(request, "Your account has been successfully created.")
            return redirect('login')
        else:
            messages.error(request,"Confirm password mismatch.")
            return redirect('register')
    return render(request, 'user_register.html')

def signin(request):
    if request.method == 'POST':
        name = request.POST['name']
        pass1 = request.POST['password']
        user = authenticate(username=name, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request,"Login successfull.")
            return redirect('index')
        else:
            messages.error(request,"Bad credentials")
            return redirect('login')
    return render(request,'user_login.html') 

def signout(request):
    logout(request)
    messages.error(request, "Logged Out succesfully!")
    return redirect('index')

def orders(request):
    if not request.user.is_authenticated:
        messages.error(request,'Login to see orders.')
        return redirect('login')
    user = request.user
    orders = Order.objects.filter(uname=user.username)
    return render(request,'orders.html',{'orders':orders})

def search(request):
    if request.method == 'POST':
        service = request.POST['search_box']
        services = Service.objects.filter(name__contains=service)
        print(services)
        return render(request,'search_page.html',{'services':services})
    return render(request,'search_page.html')

def shop(request):
    services = Service.objects.all()
    return render(request, 'shop.html', {'services':services})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phno = request.POST.get('number')
        msg = request.POST.get('msg')
        message = msg + '\n\n Phone number:' + phno
        subject = name + 'Review'
        send_mail(subject, message, 'djangovivek117@gmail.com',['vivekkumar87900@gmail.com'], fail_silently = False)
        messages.success(request,'Your feedback has been recieved.')
        return redirect('contact')
    return render(request, 'contact.html')

def category(request,service_name):
    services = Service.objects.filter(name__contains=service_name)
    return render(request, 'category.html', {'services':services})

def quick(request,service_id):
    services = Service.objects.filter(id=service_id)
    return render(request,'quickviews.html',{'services':services})
    
def test(request):
    services = Service.objects.all()
    return render(request,'test.html',{'services':services})

def proceed(request,service_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            qty = request.POST.get('qty')
            print(qty)
            user = request.user
            service = Service.objects.get(id=service_id)
            total = int(qty)*int(service.price)
            return render(request,'proceed.html',{'user':user,'service':service,'total':total})
    else:
        messages.error(request,"Login before placing an order.")
        return redirect('login')
    return render(request,'proceed.html',{'user':user,'service':service})

def checkout(request,sid,total):
    user = request.user
    service = Service.objects.get(id=sid)
    if request.method == 'POST':
        uname = user.username
        username = service.username
        sname = service.name
        phno = request.POST['phno']
        email = request.POST['email']
        pay_method = request.POST['method']
        add1 = request.POST['add1']
        add2 = request.POST['add2']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        message = request.POST['message']
        qty = total/int(service.price)
        order=Order(uname=uname, username=username,service_id=sid,service_name=sname,phno=phno,email=email,pay_method=pay_method,add1=add1,add2=add2,city=city,state=state,pincode=pincode,message=message,qty=qty,total_price=total)
        order.save()
        messages.success(request,"Service booked. We'll be reaching out to you shortly.")
        return redirect('index')
    return render(request,'checkout.html',{'user':user,'service':service})

def cancel(request,oid):
    order = Order.objects.filter(id=oid)
    order.delete()
    messages.success(request,"Order cancelled successfully.")
    return redirect('index')

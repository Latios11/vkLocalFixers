from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .models import Service, Order, Com_Order
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.core.mail import send_mail

# Create your views here.
def spsignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists.')
            return redirect('spregister')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists.')
            return redirect('spregister')
        if pass1!=pass2:
            messages.error(request,'Confirm password mismatch.')
            return redirect('spregister')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request,"Account created successfully.")
        return redirect('splogin')
    return render(request, 'sp_register.html')

def spsignin(request):
    if request.user.is_authenticated:
        print("yes")
        logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request,"Login successfull.")
            return redirect('dashboard')
        else:
            messages.error(request,"Bad credentials.")
            return redirect('splogin')
    return render(request, 'sp_login.html')

def dashboard(request):
    name = request.user.username
    ser_count = Service.objects.filter(username=name).count()
    o_count = Order.objects.filter(username=name).count()
    c_count = Com_Order.objects.filter(username=name).count()
    return render(request, 'sp_dashboard.html',{'ser_count':ser_count,'o_count':o_count,'c_count':c_count})

def splogout(request):
    logout(request)
    messages.success(request,"Logged out.")
    return redirect('index')

def addservices(request):
    if request.method == 'POST':
        username = request.user.username
        name = request.POST['name']
        price = request.POST['price']
        details = request.POST['details']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3'] 
        service = Service(username=username, name=name, price=price, details=details, image1=image1, image2=image2, image3=image3)
        service.save()
        messages.success(request,"Service added successfully.")
        return redirect('addservices')
    return render(request,'sp_products.html')

def spupdate(request):
    if request.method == 'POST':     
        old_pass = request.POST.get('old_pass')
        new_pass = request.POST.get('new_pass')
        user = request.user
        if user.check_password(old_pass):
           user.set_password = new_pass
           user.save()
           return redirect('splogin')
        else:
           return HttpResponse("error")
    return render(request, 'sp_update.html')

def services(request):
    uname = request.user.username
    services = Service.objects.filter(username=uname)
    return render(request, 'services.html', {'services': services})

def delete_service(request, service_id):
    print(service_id)
    Service.objects.filter(id=service_id).delete()
    messages.success("Service deleted.")
    return redirect('services')

def sporders(request):
    user = request.user
    orders = Order.objects.filter(username=user.username)
    services = Service.objects.filter(username=user.username)
    return render(request,'sp_orders.html',{'orders':orders,'services':services})

def back(request):
    return redirect('dashboard')

def complete(request,oid):
    order = Order.objects.get(id=oid)
    uname = order.uname
    username = order.username
    service_id = order.service_id
    service_name = order.service_name
    phno = order.phno
    email = order.email
    add1 = order.add1
    add2 = order.add2
    city = order.city
    state = order.state
    pincode = order.pincode
    total_price = order.total_price
    placed_on = order.placed_on
    send_mail(
          'LocalFixers',
          'We inform you that the service you requested has been successfully completed.\n We have devoted considerable effort and attention to detail to ensure that the outcome meets your expectations. \n\nShould you have any further questions or require additional assistance, please do not hesitate to contact us. Our dedicated team is readily available to address any concerns you may have.',
          'djangovivek117@gmail.com',
          [email],
          fail_silently=False,      
    )
    corder = Com_Order(uname=uname,username=username,service_id=service_id,service_name=service_name,phno=phno,email=email,add1=add1,add2=add2,city=city,state=state,pincode=pincode,total_price=total_price,placed_on=placed_on)
    corder.save()
    order.delete()
    return redirect('sporders')

def corders(request):
    user = request.user
    services = Service.objects.filter(username=user.username)
    com = Com_Order.objects.filter(username=user.username)
    return render(request,'completed.html',{'com':com,'services':services})
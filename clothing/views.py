from django.shortcuts import render, redirect
from product.models import Category, Subcategory, Prod
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from orderapp.models import Cartitem, Order
import datetime
from django.http import HttpResponse

def index(request):
    p= Prod.objects.all()
    cat = Subcategory.objects.all()
    return render(request, 'index.html', {'p':p, 'cat':cat})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def loginx(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'register.html')    

def handle_login(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        pass1 = request.POST.get("pass")
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)

            # messages.success(request, "Logged in")
            return redirect('home')
        else:
            # messages.info(request,'invalid credentials')
            return redirect('loginx')  
    return redirect('home')                   

def handle_signup(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if pass1==pass2:


            myuser = User.objects.create_user(username=uname, email=email, password=pass1,)
            myuser.first_name = name
            myuser.save()
            # messages.success(request, "Your account has been created")
            print('success')
            return redirect("home")
    else:

        return HttpResponse("404 error") 

def all_products(request):
    p= Prod.objects.all()
    cat= Subcategory.objects.all()
    return render(request, 'products.html', {'p':p, 'cat':cat})

def category_item(request):
    id = request.POST.get("id")
    c=Subcategory.objects.get(pk=id)
    p= Prod.objects.filter(subcat_id=id)
    cat= Subcategory.objects.all()
    return render(request, 'category_item.html', {'p':p, 'cat':cat, 'c':c})    

def product_detail(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        p= Prod.objects.get(pk=id)
        cat= Subcategory.objects.all()
        print(p)
        return render(request, 'product_detail.html', {'p':p, 'cat':cat})    
    else:

        return HttpResponse("404 error")    

def add_cart(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        p= Prod.objects.get(pk=id)
        c= Cartitem(prod_id=p.pk, quantity=1, user_id=request.user.pk)
        c.save()
        print(p)
        return redirect('home')    
    else:

        return HttpResponse("Login TO Add Cart")         
def xcart(request):
    if request.user.is_authenticated:
        c= Cartitem.objects.filter(user_id=request.user.pk)
        t=0
        for item in c:
            t=t+item.quantity*item.prod.prod_price
        return render(request, 'cart.html', {'c':c, 't':t})
    else:

        return HttpResponse("Login TO Buy")  

def handle_cart(request):
    if request.method == 'POST':
        
        c= Cartitem.objects.filter(user_id=request.user.pk)
        
        now = datetime.datetime.now()
        date_string = now.strftime("%Y%m%d%H%M%S")
        date_int = int(date_string)
        
        for item in c:
            print(item.prod)
            o=Order(prod_id=item.prod_id, quantity=item.quantity, user_id=request.user.pk, order_main_id=date_int)
            o.save()
        # c= Cartitem(prod_id=p.pk, quantity=1, user_id=request.user.pk)
        # c.save()
        
        return redirect('home')    
    else:

        return HttpResponse("Login To Order") 

def edit_cart_item(request):
    if request.user.is_authenticated:    
        if request.method=='POST':
            id= request.POST.get('id')
            
            c= Cartitem.objects.get(pk=id)
            
            return render(request, 'edit_cart.html', {'c':c})
        else:
            return HttpResponse('404 ERROR')
    else:
        return HttpResponse('Please Login')    

def handle_edit_cart_item(request):
    if request.user.is_authenticated:    
        if request.method=='POST':
            id= request.POST.get('id')
            q= request.POST.get('q')
            print('q')
            c= Cartitem.objects.get(pk=id)
            c.quantity=q
            c.save()
            return redirect('cart')
        else:
            return HttpResponse('404 ERROR')
    else:
        return HttpResponse('Please Login')

def delete_cart_item(request):
    if request.user.is_authenticated:    
        if request.method=='POST':
            id= request.POST.get('id')
            c= Cartitem.objects.get(pk=id)
            c.delete()
            return redirect('cart')
        else:
            return HttpResponse('404 ERROR')
    else:
        return HttpResponse('Please Login')  
        

def checkout(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        p= Prod.objects.get(pk=id)
        c= Cartitem.objects.filter(user_id=request.user.pk)
        t=p.prod_price
        for item in c:
            t=t+item.quantity*item.prod.prod_price
        print(p)
        return render(request, 'checkout.html', {'p':p, 'c':c, 't':t})    
    else:

        return HttpResponse("Login TO Buy")         

def handle_checkout(request):
    if request.method == 'POST':
        prod_id1 = request.POST.get("prod_id")
        p= Prod.objects.get(pk=prod_id1)
        print(p)
        c= Cartitem.objects.filter(user_id=request.user.pk)
        
        now = datetime.datetime.now()
        date_string = now.strftime("%Y%m%d%H%M%S")
        date_int = int(date_string)
        o1= Order(prod_id=p.pk, quantity=1, user_id=request.user.pk, order_main_id=date_int)
        
        for item in c:
            print(item.prod)
            o=Order(prod_id=item.prod_id, quantity=item.quantity, user_id=request.user.pk, order_main_id=date_int)
            o.save()
        # c= Cartitem(prod_id=p.pk, quantity=1, user_id=request.user.pk)
        # c.save()
        o1.save()
        print(p)
        return redirect('home')    
    else:

        return HttpResponse("Login To Order")         

def order_item(request):
    if request.user.is_authenticated:
        o= Order.objects.filter(user_id=request.user.pk)
        # cat= Subcategory.objects.all()
        return render(request, 'order_item.html', {'o':o})
    else:
        return HttpResponse("Login To Check Items")    

def logoutx(request):
    logout(request)
    return redirect('home')        

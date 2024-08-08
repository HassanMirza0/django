from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from website.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.conf import settings 
import razorpay
from django.views.decorators.csrf import csrf_exempt

client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRECT))

# Create your views here.
def index(request):
    product= Product.objects.all()
    params={ "product" : product}
    return render(request, 'indexi.html',params)
    
def index2(request):
    product= Product.objects.all()
    params={ "product" : product , "range":range(1,4)}
    return render(request, 'index.html',params)

@login_required(login_url='login_page')

def aboutus(request):
    return render(request, 'aboutus.html')

@login_required(login_url='login_page')

def products(request):
    product= Product.objects.all()
    params={ "product" : product , "range":range(3,8)}
    return render(request, 'products.html',params)


def login_page(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
 
        if not User.objects.filter(username=username).exists():
                messages.error(request, 'This Username is not registered ! please register')
                return redirect('signup')
        
        user=authenticate(username=username, password=password)


        if user is None :
            messages.error(request, 'invalid username or password')
            return redirect('login_page')   
        
        else:
          messages.success(request, 'Login successfully')
          login(request, user)
          return  redirect('/')


    return render(request, 'navlogin.html')

def logout_page(request):
    logout (request)
    return redirect('login_page')


def signup(request):
    if request.method == 'POST':
         first_name = request.POST.get('last_name')
         last_name = request.POST.get('first_name')
         username = request.POST.get('username')
         password = request.POST.get('password')
 
         user=User.objects.filter(username=username)
    
         if user.exists():
            messages.warning(request, 'Username is already taken!')

            return redirect('signup')

         user = User(first_name=first_name,last_name=last_name,username=username)

         user.set_password(password)
         user.save()
         messages.success(request, 'Account Created successfully.!')


         return redirect('signup')
    return render(request, 'signup.html')  
@login_required(login_url='login_page')

def camera(request):
    return render(request, 'camera.html')

@login_required(login_url='login_page')

def charger(request):
    return render(request, 'charger.html')

@login_required(login_url='login_page')

def headphone(request):
    return render(request, 'headphones.html')

@login_required(login_url='login_page')

def iphone(request):
    return render(request, 'iphone.html')

@login_required(login_url='login_page')

def laptop(request,myid):
    product=Product.objects.filter(id=myid)
    product_extra= Product.objects.all()

    params={ "product" : product[0],"range" : range(1,5),"product_extra" : product_extra}
    return render(request, 'laptop.html',params)

@login_required(login_url='login_page')

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
     
        contactus = Contactus(name=name, email=email,
                              phoneNo=phoneNo, date=datetime.now())
        contactus.save()
        messages.success(request, 'your form has been submitted.!')
    return render(request, 'contactus.html')

@login_required(login_url='login_page')

def smartWatch(request):
    return render(request, 'smartwatch.html')

@login_required(login_url='login_page')

def speaker(request):
    return render(request, 'speaker.html')

@login_required(login_url='login_page')

def mouse(request):
    return render(request, 'mouse.html')

@login_required(login_url='login_page')

def checkout(request):

    payment=client.order.create({
        "amount":500,
        "currency":"INR",
        "payment_capture":1

   } )
    order_id=payment['id']
    print(order_id)
    context={
        "order_id":order_id,
        "payment":payment,     
    }
   
    return render(request, 'checkout.html',context)

@login_required(login_url='login_page')

def placeorder(request):

    if request.method == 'POST':
       uid=request.session.get('_auth_user_id')
       cart=request.session.get('cart')
       user=User.objects.get(id=uid)
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       email = request.POST.get('email')
       phoneNo = request.POST.get('phoneNo')
       address = request.POST.get('address')
       houseno = request.POST.get('houseno')
       postcode = request.POST.get('postcode')
       amount = request.POST.get('amount')
       payment = request.POST.get('payment')
       order_id = request.POST.get('order_id')
    
      
       
       context={
        "order_id":order_id,
    }
      
       order=Order(
           user=user,
           first_name=first_name,
           last_name=last_name,
           email=email,
           phoneNo=phoneNo,
           address=address,
           houseno=houseno,
           postcode=postcode,
           amount=amount,
           payment_id=order_id,

       )
       order.save()


       for i in cart:
           a=float(cart[i]['price'])
           b=cart[i]['quantity']
           total=a*b
         

           item=OrderItem(
               order=order,
               Product=cart[i]['name'],
               image=cart[i]['image'],  
               quantity=cart[i]['quantity'],  
               price=cart[i]['price'],
               total=total
           )  
           item.save()

    return render(request, 'placeorder.html',context)

@login_required(login_url='login_page')

@csrf_exempt
def thankyou(request):
       
       if request.method == 'POST':
           order_id = request.POST.get('order_id')
           a=request.POST
           order_id = ""
           for key, val in a.items():
               if key == 'razorpay_order_id':
                   order_id =val

                   break
             
           user_order = Order.objects.filter(payment_id = order_id).first()
           user_order.paid = True
           user_order.save()
              
         
       return render(request, 'thankyou.html')
#cart
@login_required(login_url='login_page')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    next_url = request.GET.get('next', '/')

    # Redirect back to the current page
    return redirect(next_url)


@login_required(login_url='login_page')

def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    next_url = request.GET.get('next', '/')

    # Redirect back to the current page
    return redirect(next_url)


@login_required(login_url='login_page')

def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url='login_page')

def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url='login_page')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url='login_page')

def cart_detail(request):
    return render(request, 'cart_detail.html')
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerResgistrationForm,CustromerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Cart

class ProductView(View):
    def get(self,request):
        topvegetables=Product.objects.filter(category='TV')
       
        bottomvegetables=Product.objects.filter(category='BV')
        fruits=Product.objects.filter(category='F')
        
        
        return render(request,'app/home.html',{'topvgetables':topvegetables,'bottomvegetables':bottomvegetables,'fruits':fruits})


class ProductDetailView(View):
  def get(self,request,pk):
    product=Product.objects.get(pk=pk)
    item_already_in_cart=False
    if request.user.is_authenticated:
      item_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    return render(request,'app/productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})

@login_required
def add_to_cart(request):
  user=request.user
  product_id=request.GET.get('prod_id')
  product=Product.objects.get(id=product_id)
  Cart(user=user,product=product).save()
  return redirect('/cart')

@login_required
def show_cart(request):
  if request.user.is_authenticated:
    user=request.user
    cart=Cart.objects.filter(user=user)
   
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user == user]
    if cart_product:
      for p in cart_product:
        tempamount=(p.quantity * p.product.discount_price)
        amount+=tempamount
        total_amount=amount+shipping_amount
      return render(request,'app/addtocart.html',{'carts':cart,'total_amount':total_amount,'amount':amount})
    else:
      return render(request,'app/emptycart.html')
    


def plus_cart(request):
  if request.method =='GET':
    
    prod_id=request.GET['prod_id']
    c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity+=1
    c.save()
    amount=0.0
    shipping_amount=70.0
    cart_product=[p for p in Cart.objects.all() if p.user==request.user]
    for p in cart_product:
      tempamount=(p.quantity * p.product.discount_price)
      amount+=tempamount
      
    dat={
      'quantity':c.quantity,
      'amount' :amount,
      'totalamount':amount+shipping_amount
        
        }
    return JsonResponse(dat)
  


  
def minus_cart(request):
  if request.method =='GET':
    
    prod_id=request.GET['prod_id']
    c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity-=1
    c.save()
    amount=0.0
    shipping_amount=70.0
    cart_product=[p for p in Cart.objects.all() if p.user==request.user]
    for p in cart_product:
      tempamount=(p.quantity * p.product.discount_price)
      amount+=tempamount
      
    dat={
      'quantity':c.quantity,
      'amount' :amount,
      'totalamount':amount+shipping_amount
        
        }
    return JsonResponse(dat)
  


def remove_cart(request):
    if request.method =='GET':
    
      prod_id=request.GET['prod_id']
      c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
      
      c.delete()
      amount=0.0
      shipping_amount=70.0
      cart_product=[p for p in Cart.objects.all() if p.user==request.user]
      for p in cart_product:
        tempamount=(p.quantity * p.product.discount_price)
        amount+=tempamount
        
      dat={
        
        'amount' :amount,
        'total_amount':amount+shipping_amount
        
        
          }
      return JsonResponse(dat)
  
  


      
      
    




def buy_now(request):
 return render(request, 'app/buynow.html')





def address(request):
 add=Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

@login_required
def orders(request,data=None):
  op=OrderPlaced.filter(user=request.user)
  # if data==None:
  #  mobiles=Product.objects.filter(category='M') #yaha change krna h like mobile ki trh
  # elif data=='Redmi' or data=='Samsung':
  #   mobiles=Product.objects.filter(category='M').filter(brand=data)
  # elif data=='below':
  #      mobiles=Product.objects.filter(category='M').filter(discount_price__lt=10000)
  # elif data=='above':
  #      mobiles=Product.objects.filter(category='M').filter(discount_price__gt=10000)
  # return render(request, 'app/orders.html',{'order':'order'})
  return render(request, 'app/orders.html',{'order_placed':op})



def TopVegetable(request,data=None):
  if data==None:
   TopVegetable=Product.objects.filter(category='V')
  elif data=='Mango' or data=='Apple':
    TopVegetable=Product.objects.filter(category='V').filter(brand=data)
  elif data=='below':
       TopVegetable=Product.objects.filter(category='V').filter(discount_price__lt=10000)
  elif data=='above':
       TopVegetable=Product.objects.filter(category='V').filter(discount_price__gt=10000)
    

  return render(request, 'app/Vegetable.html',{'Vegetable':TopVegetable})

# def Vegetable(request):
#   return render(request, 'app/Vegetable.html',{'Vegetable':Vegetable})



def TopFruits(request,data=None):
  if data==None:
   TopFruits=Product.objects.filter(category='F')
  elif data=='Mango' or data=='Apple':
    TopFruits=Product.objects.filter(category='F').filter(brand=data)
  elif data=='below':
       TopFruits=Product.objects.filter(category='F').filter(discount_price__lt=10000)
  elif data=='above':
       TopFruits=Product.objects.filter(category='F').filter(discount_price__gt=10000)
    

  return render(request, 'app/Fruits.html',{'Fruits':TopFruits})



# def Fruits(request):
#   return render(request, 'app/Fruits.html',{'Fruits':Fruits})



class CustomerRegistrationView(View):
  def get(self,request):
    form=CustomerResgistrationForm()
    return render(request, 'app/customerregistration.html',{'form':form})
  def post(self,request):
    form=CustomerResgistrationForm(request.POST)
    if form.is_valid():
      messages.success(request,'congratulations !! Registered Sucessfully')
      form.save()
    return render(request, 'app/customerregistration.html',{'form':form})
  


@login_required
def checkout(request):

    user=request.user
    add=Customer.objects.filter(user=user)
    cart_items=Cart.objects.filter(user=user)
    amount=0.0
    shipping_amount=70.0
    total_amount=0.0
    cart_product=[p for p in Cart.objects.all() if p.user == user]
    if cart_product:
      for p in cart_product:
        tempamount=(p.quantity * p.product.discount_price)
        amount+=tempamount
      totalamount=amount+shipping_amount
    
    return render (request,'app/checkout.html',{'add':add,'total_amount':total_amount,'cart_items':cart_items})
  


@login_required
def payment_done(request):
  user=request.user
  custid=request.GET.get('custid') 
  customer=Customer.objects.get(id=custid)
  cart=Cart.objects.filter(user=user)
  for c in cart:
    OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
    c.delete()
  return redirect("orders")
      
   

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
  def get(self,request):
    form=CustromerProfileForm()
    return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
  
  def Post(self,request):
    form=CustromerProfileForm(request.POST)
    if form.is_valid():
      usr=request.user
      name=form.cleaned_data['name']
      locality=form.cleaned_data['locality']
      city=form.cleaned_data['city']
      state=form.cleaned_data['state']
      zipcode=form.cleaned_data['zipcode']
      reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
      reg.save()
      messages.success(request,'congratulation !! Profile Updated Sucessfully')
    return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
      

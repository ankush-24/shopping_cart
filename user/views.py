from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect ,get_object_or_404
from allauth.account.forms import LoginForm
from allauth.account.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.db import transaction
from ecom.celery import debug_task
from user import models
from user.forms import SignUpForm
from rest_framework import viewsets
from user import serializers
from user.models import Profile
from user.forms import UserForm

curl = settings.CURRENT_PATH



# Create your views here.

def home(request):
    product = models.Product.objects.all()
    print(debug_task.delay())   
    return render(request, "home.html", {"curl": curl, "product": product})


@login_required
def addtocart(request, pk):
    cart = models.Cart.objects.filter(user=request.user)
    if cart:
        cart.delete()
    product = models.Product.objects.get(pk=pk)
    cart = models.Cart.objects.get_or_create(product=product, user=request.user)
    return HttpResponseRedirect(reverse('cart'))
    # user = models.Cart.objects.all()


@login_required
def cart(request):
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        email = request.user.email
        user = request.user.username
        cart_id = request.POST.getlist("cart_id")
        sub_total = request.POST.getlist("sub-total")
        grand_total = request.POST.get("grand-total")
        total_quantity = request.POST.getlist("total-quantity")
        for item in range(len(cart_id)):
            cart = models.Cart.objects.get(id=cart_id[item])
            cart.subtotal = sub_total[item]
            cart.quantity = total_quantity[item]
            cart.save()
            cart = models.Cart.objects.filter()
            return render(
                request,
                "order.html",
                {
                    "cart": cart,
                    "grand_total": grand_total,
                    "user": user,
                    "email": email,
                },
            )
        print(debug_task.delay())    
    else:
        cart = models.Cart.objects.filter(user=request.user)
        return render(request, "cart.html", {"cart": cart})


def order(request):
    # import pdb;pdb.set_trace()
    username = request.user.username
    user = request.user

    if request.method == "POST":
        cart_items = models.Cart.objects.filter()
        for item in cart_items:
            quantity = item.quantity
            subtotal = item.subtotal
            obj = item.product
            user = item.user.username
        address = request.POST.get("user_address")
        grand_total = request.POST.get("grand_total")
        orderitems = models.Order.objects.create(
            orderitems=obj,
            user_address=address,
            grandtotal=grand_total,
            quantity=quantity,
            subtotal=subtotal,
            user=request.user,
        )
        cart_items.delete()
        return HttpResponseRedirect(reverse('order'))
    else:
        orderitems = models.Order.objects.filter(user=request.user)
        return render(request, "orderitems.html", {"orderitems": orderitems})


def delete(request, pk):
    user = models.Cart.objects.get(pk=pk)
    user.delete()
    return HttpResponseRedirect(reverse('cart'))

class ProductViewset(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class CartViewset(viewsets.ModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer    


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')        

# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return HttpResponseRedirect('/')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'home/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })


# def changepass(request):
#     if request.method=='GET':
#         return render(request,'changepass.html',{'curl':curl,'sunm':request.session['sunm'],'output':''})
#     else:
#         opass = request.POST.get('opass')
#         npass  = request.POST.get('npass')
#         cnpass = request.POST.get('cnpass')

#         userdetails = models.register.objects.filter(username=request.session['sunm'],password=opass)
#         if len(userdetails)>0:
#             if npass==cnpass:
#                 models.register.objects.filter(username=request.session['sunm'],password=opass).update(password=npass)
#                 return render(request,'changepass.html',{'curl':curl,'sunm':request.session['sunm'],'output':'Password Change Successfully'})   
#             else:
#                 return render(request,'changepass.html',{'curl':curl,'sunm':request.session['sunm'],'output':'New Password and confirm new password MisMatch'})             
#         else:
#             return render(request,'changepass.html',{'curl':curl,'sunm':request.session['sunm'],'output':'Invalid Old Password'})       

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from motors.models import Products,Wish_Product,WishList
from django.contrib.auth.decorators import login_required


def home(request):
    vehicle_obj=Products.objects.filter(sold=False)
    context={
    'vehicle_obj':vehicle_obj
    }
    return render(request,'motors/products.html',context)
def ProductDetailsView(request,id):
    veh=Products.objects.get(id=id)
    context={
    'vehicle':veh
    }
    return render(request,'motors/product_details.html',context)
@login_required
def AddToWishList(request,id):
    wish_brand=Products.objects.get(id=id)
    wish_prod,created=Wish_Product.objects.get_or_create(wish_brand=wish_brand,user=request.user,sold=False)
    list=WishList.objects.filter(user=request.user,sold=False)
    if list.exists():
        list=list[0]
        if list.wish_brands.filter(wish_brand__id=wish_brand.id).exists():
            wish_prod.save()
        else:
            list.wish_brands.add(wish_prod)
    else:
        list=WishList.objects.create(user=request.user)
        list.wish_brands.add(wish_prod)
    return HttpResponseRedirect(f'/mywishlist/')
@login_required
def RemoveFromWishListView(request,id):
    wish_brand=Products.objects.get(id=id)
    wish_prod=Wish_Product.objects.get_or_create(wish_brand=wish_brand,user=request.user,sold=False)
    list=WishList.objects.filter(user=request.user,sold=False)
    if list.exists():
        list=list[0]
        if list.wish_brands.filter(wish_brand__id=wish_brand.id).exists():
            wish_prod=Wish_Product.objects.filter(user=request.user,sold=False)[0]
            list.wish_brands.remove(wish_prod)
        else:
            print('successfully deleted!!'*100)
            return HttpResponseRedirect('/mywishlist/')
    else:
        print('successfully deleted!!!'*100)
        return HttpResponseRedirect('/mywishlist/')
    return HttpResponseRedirect('/mywishlist/')

@login_required
def WishListView(request):
    mylist=WishList.objects.filter(user=request.user,sold=False)
    context={
    'mylist':mylist
    }
    return render(request,'motors/wish_summary.html',context)

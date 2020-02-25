from django.urls import path
from motors import views
app_name="motors"


urlpatterns=[
path('',views.home,name="home"),
path('product/details/<id>/',views.ProductDetailsView,name="details"),
path('AddToWhish/<id>/',views.AddToWishList,name="add_wish"),
path('mywishlist/',views.WishListView,name="list"),
path('removefromwishlist/<id>/',views.RemoveFromWishListView,name="remove")
]

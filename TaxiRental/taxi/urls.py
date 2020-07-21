from django.urls import include ,path
from . import views

urlpatterns = [
   path("",views.index,name="HomePage"),
   path("info/",views.info,name="Information"),
   path("contact/",views.contact, name="Contact Us"),
   path("dashboard/",views.dashboard,name="Dashboard"),
   path("signin/", views.sign_in, name="signin"),
   path("callback", views.callback, name="callback"),
   path("checkout/",views.checkout, name="checkout"),
   path("payment/",views.payment, name="payment"),
]
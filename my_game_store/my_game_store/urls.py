from django.urls import path
#from task1.views import *
from task1.views import home_view, store_view, cart_view, sign_up_by_django

urlpatterns = [
    path('', home_view, name='home'),
    path('store/', store_view, name='store'),
    path('cart/', cart_view, name='cart'),
    path('registration/', sign_up_by_django, name='registration'),
]

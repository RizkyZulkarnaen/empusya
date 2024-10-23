from django.urls import path
from .views import ecommerce

urlpatterns = [
    path('', ecommerce.eCommerce, name='ecommerce'),
]
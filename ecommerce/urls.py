from django.urls import path
from .views import ecommerce, shopee

urlpatterns = [
    path('', ecommerce.eCommerce, name='ecommerce'),
    path('shopee/scrape', shopee.scrape_shopee, name='scrapeShopee'),
]
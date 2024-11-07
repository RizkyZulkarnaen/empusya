from django.shortcuts import render
from bs4 import BeautifulSoup

def scraping():
    pass

def scrape_shopee(request):
    return render(request, 'e-commerce/shoppe/scrape_product.html', {})
from django.shortcuts import render
from bs4 import BeautifulSoup

def scrapeShopee(request):
    return render(request, 'e-commerce/shoppe/scrape_product.html', {})
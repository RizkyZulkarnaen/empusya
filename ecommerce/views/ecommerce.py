from django.shortcuts import render

def eCommerce(request):
    return render(request, 'e-commerce/eCommerce.html', {})
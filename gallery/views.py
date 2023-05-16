from django.shortcuts import render


# Create your views here.
def baby(request):
    return render(request,'gallery/baby.html')


def country(request):
    return render(request,'gallery/country.html')


def product(request):
    return render(request,'gallery/product.html')
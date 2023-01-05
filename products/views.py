from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# whenever is a request to: /products call index()
# So to make this function 'work' we need to map /products to index()!
# We will create a new .py file (module) and name it url
def index(request):
    products = Product.objects.all()
    return render(request,
                  'index.html',
                  {'products': products}
                  )


def new(request):
    return HttpResponse('Welcome to new page')

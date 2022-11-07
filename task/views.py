from django.shortcuts import render, redirect
from .forms import Add_Product
from .models import Product
from django.contrib import messages


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def add_new_product(request):
    if request.method == 'POST':
        print(request.method)
        form = Add_Product(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Add_Product()
        return render(request , 'add_new_product.html',{'form':form})
    return render(request, 'add_new_product.html',{'form':form})

def update_product(request,id):
    if request.method =='POST':
        update_product = Product.objects.get(pk = id)
        print(update_product)
        form = Add_Product(request.POST, instance=update_product)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        update_product = Product.objects.get(pk = id)
        form = Add_Product(instance=update_product)
    return render(request,'update_product.html',{'form':form})

def search(request):
    query = request.GET.get('get_query')
    print(query)
    product_search_match = Product.objects.filter(product_name__icontains = query)
    return render(request, 'search.html',{'product_search_match':product_search_match})
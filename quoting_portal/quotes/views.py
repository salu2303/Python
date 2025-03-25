from django.shortcuts import render,redirect

# Create your views here.
from django.http import JsonResponse
from .models import Product, Quote
from .forms import QuoteForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'quotes/product_list.html', {'products': products})

def create_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_success')
    else:
        form = QuoteForm()
    return render(request, 'quotes/create_quote.html', {'form': form})

def quote_success(request):
    return render(request, 'quotes/quote_success.html')


def get_price(request):
    product_id = request.GET.get('product_id')
    quantity = int(request.GET.get('quantity', 1))
    product = Product.objects.get(id=product_id)
    total_price = product.price_per_unit * quantity
    return JsonResponse({'total_price': total_price})

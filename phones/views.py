from django.shortcuts import render, redirect
from phones.models import Phone



def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get("sort")
    if sorting == 'name':
        phones_obj = Phone.objects.order_by('name')
    elif sorting == 'min_price':
        phones_obj = Phone.objects.order_by('price')
    else:
        phones_obj = Phone.objects.all()
    phones_list = list(phones_obj)
    context = {
        'our_catalog': phones_list
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_obj = Phone.objects.all()
    phones_list = list(phones_obj)
    context = {}
    for phone in phones_list:
        if slug != phone.slug:
            continue
        else:
            context = {
                'phone': phone
            }
            break

    return render(request, template, context)

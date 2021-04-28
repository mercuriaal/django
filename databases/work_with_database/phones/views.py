from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    sorting = request.GET.get('sort')
    if sorting == 'name':
        context['phones'] = Phone.objects.all().order_by('name')
    elif sorting == 'min_price':
        context['phones'] = Phone.objects.all().order_by('price')
    elif sorting == 'max_price':
        context['phones'] = Phone.objects.all().order_by('-price')
    else:
        context['phones'] = Phone.objects.all()
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}

    context['properties'] = Phone.objects.filter(slug=slug)

    return render(request, template, context)

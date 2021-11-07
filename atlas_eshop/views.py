import itertools

from django.shortcuts import render
from eshop_sliders.models import Slider
from eshop_product.models import Product
from eshop_settings.models import SiteSettings


def grouper(n,iterable):
    args=[iter(iterable)] * n
    return [(e for e in t if e is not None) for t in itertools.zip_longest(*args)]


def home_page(request):
    most_viewed=Product.objects.order_by('-visit_count').all()[:8]
    latest_products=Product.objects.order_by('-id').all()[:8]
    sliders=Slider.objects.all()
    context={
        'sliders':sliders,
        'most_viewed':grouper(4,most_viewed),
        'latest_products':grouper(4,latest_products)
    }
    return render(request,"home_page.html",context)


def about_us(request):
    settings = SiteSettings.objects.first()
    context = {
        'settings': settings
    }
    return render(request, "about_us.html", context)


def footer(request):
    settings=SiteSettings.objects.first()
    context={
        'settings':settings
    }
    return render(request,"shared/Footer.html",context)


def header(request):
    settings = SiteSettings.objects.first()
    context = {
        'settings': settings
    }
    return render(request,"shared/Header.html",context)


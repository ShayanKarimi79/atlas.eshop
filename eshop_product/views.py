import django.http
from django.shortcuts import render
from .models import Product,ProductGallery
from eshop_products_category.models import  ProductCategory
from eshop_orders.forms import UserNewOrderFom
from django.views.generic import ListView,DetailView
from django.http import Http404
import itertools


def grouper(n,iterable):
    args=[iter(iterable)] * n
    return [(e for e in t if e is not None) for t in itertools.zip_longest(*args)]


class ProductsList(ListView):
    template_name = "products/product_list.html"
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()

class ProductsListByCategory(ListView):
    template_name = "products/product_list.html"
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        category_slug=self.kwargs['category']
        category=ProductCategory.objects.filter(slug__iexact=category_slug).first()
        if category is None:
            raise Http404("category not found")
        else:
            return Product.objects.get_by_category(category_slug)




def product_detail(request,*args,**kwargs):
    productId=kwargs['productId']
    order_form = UserNewOrderFom(request.POST or None,initial={'product_id':productId})
    product : Product =Product.objects.get_by_id(productId)

    if product is None:
        raise Http404()
    product.visit_count+=1
    product.save()

    gallery=ProductGallery.objects.filter(product_id=productId)
    grouped_gallery=list(grouper(3,gallery))
    related_products=Product.objects.get_queryset().filter(categories__product=product).distinct()
    print(related_products)
    grouped_related_products=list(grouper(3,related_products))
    context={
        'product':product,
        'galleries':grouped_gallery,
        'related_products':grouped_related_products,
        'order_form':order_form
    }
    return render(request,"products/product_detail.html",context)


class search(ListView):
    template_name = "products/product_list.html"
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        query=self.request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)


        return Product.objects.get_active_products()


def products_categories_partial(request):
    categories=ProductCategory.objects.all()
    context={'categories':categories}
    return render(request,"products/product_categories_partial.html",context)

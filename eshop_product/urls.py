from django.urls import path
from .views import ProductsList, product_detail, search,ProductsListByCategory,products_categories_partial

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/search', search.as_view()),
    path('products/<int:productId>', product_detail),
    path('products/<str:category>', ProductsListByCategory.as_view()),
    path('products_categories_partial', products_categories_partial,name='products_categories_partial')

]

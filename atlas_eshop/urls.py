"""atlas_eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.conf.urls.static
from django.contrib import admin
from django.urls import path,include
from atlas_eshop import settings
from django.conf.urls.static import static
from .views import home_page,footer,header,about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('eshop_account.urls')),
    path('',include('eshop_product.urls')),
    path('',include('eshop_contact.urls')),
    path('',include('eshop_orders.urls')),
    path('',home_page),
    path('about-us',about_us),
    path('footer',footer,name="footer"),
    path('header',header,name="header")

]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
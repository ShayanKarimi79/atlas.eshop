from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from eshop_settings.models import SiteSettings

# Create your views here.


def contact_page(request):
    form=ContactForm(request.POST or None)
    settings=SiteSettings.objects.first()

    if form.is_valid():
        fullname=form.cleaned_data.get('fullname')
        subject=form.cleaned_data.get('subject')
        message=form.cleaned_data.get('message')
        email=form.cleaned_data.get('email')
        Contact.objects.create(fullname=fullname,subject=subject,message=message,email=email)
        #todo:show user a success message
        form=ContactForm()

    context={
        'form':form,
        'settings':settings
     }
    return render(request,"contact/contact_us_page.html",context)
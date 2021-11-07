from django import forms
from django.core import validators


class ContactForm(forms.Form):
    fullname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'نام خود را بنویسید','class':'form-control'}),label="نام و نام خانوادگی",
                             validators=[validators.MinLengthValidator(50, "حداکثر طول نام 50 کاراکنر است")])

    subject = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'عنوان پیام','class':'form-control'}), label="موضوع"
                              , validators=[validators.MinLengthValidator(80, "حداکثر طول عنوان 80 کاراکنر است")])

    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'ایمیل خود را وارد کنید' ,'class':'form-control'}),label="ایمیل",
                           validators=[validators.MinLengthValidator(50, "حداکثر طول ایمیل 50 کاراکنر است")])

    message=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'پیام شما','class':'form-control','rows':8}),label="متن پیام",
                            validators=[validators.MinLengthValidator(500, "حداکثر طول متن 500 کاراکنر است")])



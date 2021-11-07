from django import forms
from django.contrib.auth.models import User
from django.core import validators

class EditUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "ایمیل خود را وارد کنید",'class':'form-control'}), label="Email")



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "لطفا نام خود را وارد نمایید"}),
                               label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "لطفا رمز خود را وارد نمایید"}),
                               label="رمز عبور")


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "نام گاربری خود را وارد کنید"}),
                               label="نام کاربری")
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "ایمیل خود را وارد کنید"}), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور خود را وارد کنید"}),
                               label="رمز عبور",
                               validators=[validators.MinLengthValidator(8, "حداقل طول رمز عبور 8 کاراکنر است")])
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور خود را تکرار کنید"}),
                                  label="تکرار رمز عبور")

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError("رمز عبور با تکرار آن مغایرت دارد")
        return re_password

    def clean_username(self):
        username = self.cleaned_data.get("username")
        isExist = User.objects.filter(username=username).exists()
        if isExist:
            raise forms.ValidationError("نام کاربری قبلا ثبت شده")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        isExist = User.objects.filter(email=email).exists()
        if isExist:
            raise forms.ValidationError("ایمیل قبلا ثبت شده")
        return email
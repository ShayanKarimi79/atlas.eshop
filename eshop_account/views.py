import django.http
from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm,EditUserForm
from django.contrib.auth import login,get_user_model,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404




def log_in(request):
    loginForm=LoginForm(request.POST or None)
    if  loginForm.is_valid():
        username=loginForm.cleaned_data.get("username")
        password=loginForm.cleaned_data.get("password")
        user =authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            loginForm.add_error("username","نام کاربری یا رمز عبور اشتباه است")
    context={"form":loginForm}
    return render(request,'account/login.html',context)



def register (request):
    register_form=RegisterForm(request.POST or None)
    if register_form.is_valid():
        username=register_form.cleaned_data.get("username")
        email=register_form.cleaned_data.get("email")
        password=register_form.cleaned_data.get("password")
        user=User.objects.create_user(username=username,email=email,password=password)
        login(request,user)
        redirect('/')
    context={"form":register_form}
    return render(request,'account/register.html',context)


def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_profile_page(request):
    context={}
    return render(request,"account/user_account_page.html",context)


@login_required(login_url='/login')
def edit_user_profile(request):
    user=User.objects.get(id=request.user.id)
    if user is None:
        raise Http404("کاربر وجود ندارد")

    edit_user_form=EditUserForm(request.POST or None,initial={'email':user.email})
    if edit_user_form.is_valid():
        user.email=edit_user_form.cleaned_data.get('email')
        user.save()

    context = {'form':edit_user_form}
    return render(request, "account/edit_user_profile.html", context)


def profile_sidebar(request):
    return render(request,"account/user_sidebar.html",)
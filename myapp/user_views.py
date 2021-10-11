from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render,redirect,get_list_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

def register_user(request):
    form = RegisterForm()
    if request.method=='POST':
        # print(request.POST)
        form= RegisterForm(request.POST)
        if form.is_valid():
            form.save_user()
            return redirect("index")
    return render(
        request=request,
        template_name='user/register.html',
        context={
            'form':form
        }
    )

def login_user(request):
    form = LoginForm()
    message = ""
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Hàm authenticate nhận username và password
            # Nếu thông tin đúng thì return User Object
            # Không đúng thì return None
            user = authenticate(
                username=form.cleaned_data['username'],
                password= form.cleaned_data['password'],
            )
            if user: # Kiem tra not None la True
                # print('Thông tin đúng')
                # Thông tin đúng giữ trạng thái đăng nhập user
                login(request,user)
                # Thay vì kiểm tra redirect về index, phải kiểm tra cái tham số getnext trên web
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                return redirect ('index')
            else:
                # print('Thông tin sai')
                message = " Thông tin nhập không đúng.Vui lòng nhập lại"

    return render(
        request=request,
        template_name='user/login.html',
        context={
            'form':form,
            'message' : message
        }
    )




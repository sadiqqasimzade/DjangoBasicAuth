from django.shortcuts import render,redirect,resolve_url
from django.views import View
from django.contrib.auth import login
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html',{'form':NewUserForm()})

    def post(self,request):
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(resolve_url('/'))

        return render(request, 'register.html', { 'form': form })

class LoginView(View):
    def get(self,request):
        return render(request,'login.html',{'form':AuthenticationForm()})


    def post(self,request):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(resolve_url('/'))
        return render(request, 'login.html', { 'form': AuthenticationForm() })


def logout_user(request):
    logout(request)
    return redirect(resolve_url('/'))
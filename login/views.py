from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, 
                        password = password)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error (request, "Credenciais Inválidas")
    
    return render(request, 'login/login.html')


def logout_user(request):
    logout(request)

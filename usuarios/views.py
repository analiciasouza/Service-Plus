from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from .models import User
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
    
    return render(request, 'usuarios/login.html')


def logout_user(request):
    logout(request)


def create_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        day_of_birth = request.POST.get("day_of_birth")
        type_user = request.POST.get("type_user")
        password = request.POST.get("password")

        if not name or not email or not day_of_birth or not password:
                messages.error (request, "Campos Obrigatórios")

        try:
            user = User.objects.create_user(name=name, 
                                    email=email, 
                                    day_of_birth=day_of_birth, 
                                    type_user=type_user, 
                                    password=password)
            return redirect('home')

        except Exception:
            error_message = f"Ocorreu um erro ao cadastrar: {Exception}"
            return render(request, 'usuarios/cadastro.html', {'error_message': error_message})

    return render(request, 'usuarios/cadastro.html')        

         
        
    
    




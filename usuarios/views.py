from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .utils import password_is_valid
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
import hashlib

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not password_is_valid(request, senha, confirmar_senha):
            return redirect('/auth/cadastro')

        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            usuario = User(username=nome, email=email, password=senha, is_active=True)
            usuario.save()

            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso !!!')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro/')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        senha = hashlib.sha256(senha.encode()).hexdigest()
        user = auth.authenticate(email=email, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/login')
        else:
            # se o usuário existe no banco de dados, é feita a autenticação do mesmo
            auth.login(request, user)
            return redirect('/home')

def sair(request):
    auth.logout(request)
    return redirect('/auth/login')


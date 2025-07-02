from django.urls import path
from django.http import HttpResponce

def product(request, id):
    if id > 0:
        return HttpResponce(f"Товар с ID: {id}")
    else:
        return HttpResponce(f"Ошибка: ID должен быть положительным")
    

def profile(request,username,post_id):
    return HttpResponce(f"Пользователь: {username}, пост №{post_id}")

def greeting(request,name,language="русский"):
    return HttpResponce(f"Привет, {name}! Язык: {language}")
    

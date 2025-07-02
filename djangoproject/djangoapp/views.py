from django.urls import path
from django.http import HttpResponce, HttpResponseBadRequest

def product(request, id):
    try:
        id_int = int(id)
        if id_int > 0:
            return HttpResponce(f"Товар с ID: {id_int}")
        else:
            return HttpResponseBadRequest(f"Ошибка: ID должен быть положительным")
    except ValueError:
        return HttpResponseBadRequest("Ошибка: ID должен быть числом")

def profile(request,username,post_id):
    return HttpResponce(f"Пользователь: {username}, пост №{post_id}")

def greeting(request,name,language="русский"):
    return HttpResponce(f"Привет, {name}! Язык: {language}")
    

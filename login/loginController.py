import requests
from django.http import HttpResponse
from django.shortcuts import redirect
import json
from django.contrib import messages


def login_con(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    response = requests.post('https://recruitment.fisdev.com/api/login/', {'username': username, 'password': password})
    text = response.text
    obj = json.loads(text)
#    print(obj['token'])
    if obj['success']:
        request.session['token'] = obj['token']
        return HttpResponse("login Done")
    else:
        messages.error(request, 'username or password not correct')
        return redirect('/login/')


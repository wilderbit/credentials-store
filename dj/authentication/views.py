from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout, login
from . import models

# Create your views here.


def login_api(req):
    body = json.loads(req.body)
    u = authenticate(email=body['email'], password=body['password'])
    if u is None:
        return JsonResponse({'data': {}, 'success': False}, status=401)
    return JsonResponse({'data': {'token': u.token}, 'success': True}, status=200)


def register(req):
    body = json.loads(req.body)
    u = models.User.objects.create_user(email=body['email'], password=body['password'])

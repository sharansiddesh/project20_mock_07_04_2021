from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def page3(request,data):
    return HttpResponse(f'the message is : {data}')



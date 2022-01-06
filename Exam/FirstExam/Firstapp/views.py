from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add(response, num1, num2):
    return HttpResponse(f'<h1>{num1 + num2}</h1>')


def minus(response, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(f'<h1>{num1 - num2}</h1>')


def div(response, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    return HttpResponse(f'<h1>{round(num1/num2)}</h1>')

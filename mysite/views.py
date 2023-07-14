from django.shortcuts import render
from django.http import request
# Create your views here.
def home(request):
    return render(request,'mysite/home.html')

def detail(request):
    return render(request,'mysite/detail.html')
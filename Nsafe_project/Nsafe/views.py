from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def index(request):
    return render(request,"index.html")

def signin(request):
    return render(request,"signin.html")

def signup(request):
    

    return render(request, 'signup.html')   
    

   


def contact(request):
    return render(request,"contact.html")

def admin(request):
    return render(request,"admin.html")

def scan(request):
    return render(request,"scan.html")



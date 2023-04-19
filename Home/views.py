from re import U
from django.shortcuts import redirect, render, HttpResponse
from Home.models import Signup
from Home.models import SignupEWC
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        u_name = request.POST.get('u_name')
        u_email = request.POST.get('u_email')
        u_password = request.POST.get('u_password')
        u_rpassword = request.POST.get('u_rpassword')

        if u_password==u_rpassword:
            signup = Signup(u_name=u_name, u_email=u_email, u_password=u_password, u_rpassword=u_rpassword)
            signup.save()
            messages.success(request, 'Profile is created')
        elif u_password != u_rpassword:
            print('password is not matching')
            messages.info(request, 'password is not matching')

    return render(request, 'signup.html')    

def earnwithyourcar(request):
    return render(request, 'earnwithyourcar.html')    

def carlist(request):

    return render(request, 'carlist.html')  

def loginEWC(request):
    return render(request, 'loginEWC.html')  

def signupEWC(request):
    if request.method == "POST":
        d_name = request.POST.get('d_name')
        d_email = request.POST.get('d_email')
        d_password = request.POST.get('d_password')
        d_rpassword = request.POST.get('d_rpassword')

        if d_password==d_rpassword:
            signupEWC = SignupEWC(d_name=d_name, d_email=d_email, d_password=d_password, d_rpassword=d_rpassword)
            signupEWC.save()
            messages.success(request, 'Profile is created')
        elif d_password!=d_rpassword:
            print('password is not matching')
            messages.info(request, 'password is not matching')
    return render(request, 'signupEWC.html')  


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index2(request):
    return render(request, 'index2.html')

def carlistl(request):
    return render(request, 'carlistl.html')    

def booked(request):
    return render(request, 'booked.html')
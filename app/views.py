from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login, authenticate


def home(request):
    return render(request,"home.html")

def register(request):
 
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        profile_picture = request.POST['profile_picture']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        Address = request.POST['address']
        Address1 = request.POST['address1']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is already exist')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.set_password(password)
                user.save()
             
                return redirect("login_user")
    else:
        print("this is not post method")

        return render(request,"register.html")
'''      
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'invalid username and password')
            return redirect('login_user')
    else:
         return render(request,"login.html")
         '''

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
'''
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user_type == 'doctor':
                return redirect('doctor_dashboard')
            elif user_type == 'patient':
                return redirect('patient_dashboard')
        else:
            messages.info(request, 'Invalid username and password')
            return redirect('login_user')
    else:
         return render(request, "login.html")
         '''
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or dashboard page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')



'''
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_type = request.POST.get('login_type')

        # Perform your authentication logic here
        # Assuming you have authenticated the user and stored it in 'user'

        if login_type == 'doctor':
            # Redirect to doctor dashboard
            return redirect('doctor_dashboard.html')
        elif login_type == 'patient':
            # Redirect to patient dashboard
            return redirect('patient_dashboard.html')

    return render(request, 'home.html')
    '''

def logout_user(request):
    auth.logout(request)
    return redirect('home')




def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')







    



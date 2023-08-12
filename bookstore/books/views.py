from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserLogin, FormRegister

def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = UserLogin.objects.filter(email=email, password=password).first()

        if user is not None:
            request.session['is_logged_in'] = True
            request.session['user_id'] = user.email
            user.active = True
            user.save()
            return redirect('index')
        else:
            # If the user is not found or the password is incorrect, show an error message.
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    # If the request method is GET, render the login page.
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST["email"]
        password_first = request.POST["password"]
        password_confirm = request.POST["Confirm_Password"]
        password = ""
        if password_first == password_confirm:
            password = password_confirm
        else:
            messages.error(request, "Passwords do not match. Please reload this page and type agin")
            return redirect('register')
        if username and password:
            user = UserLogin(email=username, password=password)
            user.save()
            return redirect('login')
    return render(request, 'register.html')

def loghome(request):
    if request.session.get('is_logged_in'):
        if request.method == "POST":
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            dob = request.POST["dob"]
            age = request.POST["age"]
            gender = request.POST["age"]
            email = request.POST["email"]
            address = request.POST["address"]
            department = request.POST["departments"]
            course = request.POST["courses"]
            purpose = request.POST["purpose"]
            book = request.POST.get("note_book", "")
            pen = request.POST.get("pen")
            paper = request.POST.get("paper")
            matirial_list = str([book, pen, paper])
            form = FormRegister(firstname=fname, lastname=lname, DOB=dob, age=age, gender=gender, email=email,
                                address=address, department=department, course=course, purpose=purpose,
                                metrials=matirial_list)
            form.save()
            return redirect('order')
    else:
        return redirect('login')
    return render(request, 'Form.html')

def order(request):
    if request.session.get('is_logged_in'):
        user_id = request.session['user_id']
        user = UserLogin.objects.filter(email=user_id).first()
        if user.active == True:
            return render(request, 'OrderConfirmation.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def index(request):
    if request.session.get('is_logged_in'):
        user_id = request.session['user_id']
        user = UserLogin.objects.filter(email=user_id).first()
        if user.active == True:
            return render(request, 'loghome.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def contact(request):
    return render(request, 'contact.html')


def logout(request):
    if request.session.get('is_logged_in'):
        user_id = request.session['user_id']
        user = UserLogin.objects.filter(email=user_id).first()
        if user is not None:
            user.active = False
            user.save()
    request.session.clear()
    return redirect('home')

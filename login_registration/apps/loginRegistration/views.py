from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from apps.loginRegistration.models import *
import bcrypt


def home(request):
    
    return render(request,"loginRegistration/index.html")

def users_create(request):
    password =''
    newuser = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'birth_date': request.POST['birth_date'],
        'password': request.POST['password'],
        'confpassword': request.POST['confpassword'],
    }
    errors = Users.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = bcrypt.hashpw(newuser['password'].encode(), bcrypt.gensalt())
        user = Users.objects.create(first_name=newuser['first_name'],last_name=newuser['last_name'],birth_date=newuser['birth_date'],email=newuser['email'],password=password.decode())
        request.session['email']=user.email
        return redirect('/users/'+str(user.id))

    

def users_show(request,id):
    if 'email' not in request.session:
        messages.add_message(request, messages.ERROR, "Please Login to view your data")
        return redirect('/')
    user = Users.objects.get(id=id)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'birth_date': user.birth_date,
        'email': user.email,
        'updated_at': user.updated_at,
    }
    if user.email == request.session['email']:
        return render(request,"loginRegistration/users_show.html",context)
    else:
        user = Users.objects.get(email=request.session['email'])
        messages.add_message(request,messages.ERROR,"You can only view your own user page")
        return redirect('/users/'+str(user.id))
def users_login(request):
    user ={
        'email': request.POST['email'],
        'password': request.POST['password']
    }
    account = Users.objects.get(email=user['email'])
    if bcrypt.checkpw(user['password'].encode(), account.password.encode()):
        request.session['email'] = user['email']
        return redirect('/users/'+str(account.id))
    else:
        return redirect('/')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect('/')

    
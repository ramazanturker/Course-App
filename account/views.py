from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.method == "POST":
        if request.user.is_authenticated and "next" in request.GET:
            return render(request, 'account/login.html', { "error": "access denied. you are not authorized" })
        
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            nextUrl = request.GET.get("next", None)
            if nextUrl is None:
                return redirect("index")
            else:
                return redirect(nextUrl)
        else:
            return render(request, 'account/login.html', { "error": "incorrect username or password" })
    else:
        return render(request, 'account/login.html')

def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password != repassword:
            return render(request, 'account/register.html', 
            { 
                "error": "password does not match",
                "username": username,
                "email": email
            })
        
        if User.objects.filter(username = username).exists():
            return render(request, 'account/register.html', 
            { 
                "error": "this username already exists please use a different username",
                "username": username,
                "email": email
            })
        
        if User.objects.filter(email = email).exists():
            return render(request, 'account/register.html', 
            { 
                "error": "this email already exists please use a different email",
                "username": username,
                "email": email
            })
        
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()
        return redirect("user_login")
            
    else:
        return render(request, 'account/register.html')

def user_logout(request):
    logout(request)
    return redirect("index")
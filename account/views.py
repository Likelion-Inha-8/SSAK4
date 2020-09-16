from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import User
# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return redirect('home')
        else :
            return HttpResponse("로그인 실패. 다시 시도해보세요")
    return render(request, 'signin.html')

def signup(request):
    if request.method=="POST":
        print(request.POST)
        username= request.POST["username"]
        password= request.POST["password"]
        dog_name = request.POST["dog_name"]
        dog_gender = request.POST["dog_gender"]
        dog_type = request.POST["dog_type"]
        dog_birth_year =request.POST["dog_birth_year"]
        dog_birth_month =request.POST["dog_birth_month"]
        dog_birth_day=request.POST["dog_birth_day"]
        dog_Image =request.FILES["dog_Image"]

        user = User.objects.create_user(username,"",password)
        user.dog_name=dog_name
        user.dog_gender=dog_gender
        user.dog_type=dog_type
        user.dog_birth_year=dog_birth_year
        user.dog_birth_month=dog_birth_month
        user.dog_birth_day=dog_birth_day
        user.dog_Image=dog_Image
        user.save()
        login(request, user)
        return redirect("home")
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')

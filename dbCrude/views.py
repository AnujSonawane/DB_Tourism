from django.shortcuts import render,HttpResponse,redirect
from .models import user1
from .forms import detailsform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html")

def loginUser(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            return render(request,"login.html")
    return render(request,"login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")

def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"about.html")

def create(request):
    if request.user.is_anonymous:
        return redirect("/login")
    elif request.method =="POST":
        nameC = request.POST["name"]
        emailC = request.POST["email"]
        describeC = request.POST["describe"]

        obj = user1.objects.create(user_name=nameC,user_email=emailC,user_opinion=describeC)
        obj.save()
        return redirect("/display/")

def display(request):
    if request.user.is_anonymous:
        return redirect("/login")
    details = user1.objects.all()
    dict1 = {
        "display":details,
    }
    return render(request,"display.html",dict1)

def addUser(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"newUser.html")

def edit(request,id):
    if request.user.is_anonymous:
        return redirect("/login")
    object = user1.objects.get(id=id)
    dict1 = {
        "s1":object
    }
    return render(request,"updateUser.html",dict1)

def update(request,id):
    if request.user.is_anonymous:
        return redirect("/login")
    object=user1.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid():
        form.save()
        object=user1.objects.all()
    return redirect('display')

def delete(request,pk):
    if request.user.is_anonymous:
        return redirect("/login")   
    user1.objects.filter(id=pk).delete()
    return redirect('display')


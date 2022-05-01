from django.shortcuts import  get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from new_app.models import CustomUser
from .forms import NewUserForm



# Create your views here.
def index(request):
    message = "Welcome to Sangharsh Foundation & Welfare Society...!"
    if request.user.is_authenticated:
        return render(request, "base.html", {'message':message, 'user':request.user})
    return render(request, "base.html", {'message':message+" - login please"})
    # return HttpResponse()
    

@login_required
def register_request(request):

    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("view_members")
        else:
            return render (request=request, template_name="register.html", context={"form":form})

    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"form":form})


@login_required
def view_members(request):
    return render(request, 'view_members.html', {'data':CustomUser.objects.all()})


def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, request.POST)
        email = request.POST['username']
        password = request.POST['password']
        # username = CustomUser.objects.get(email=email.lower()).username
        # if form.is_valid():
        user = authenticate(request, username=email, password=password)
        print(user,email,password)
        if user is not None:
            login(request, user)
            print("Loged in")
            return redirect("index")

        else:        
            return render(request=request, template_name="login.html", context={"form":form})
            
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form":form})


@login_required
def logout_request(request):
	logout(request)
	return redirect("index")


def view_card(request,id):
    instance = get_object_or_404(CustomUser, id=id)
    return render(request, "print_card.html", {'data':instance})

def delete_user(request, id):
    instance = get_object_or_404(CustomUser, id=id)
    instance.delete()
    return redirect("view_members")
    
from urllib import request
from django.http import JsonResponse
from django.shortcuts import  get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from new_app.models import Contact, CustomUser
from .forms import NewUserForm, UpdateProfileForm, UpdateUserFormAdmin



def index(request):
    print(request.method)
    if request.method == "POST":
        print("post method called")
        
    return render(request, "index.html")

@login_required
def dashbord(request):
    return render(request, "user/dashbord.html")
    

@login_required
def register_request(request):

    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("view_members")
        else:
            return render (request=request, template_name="user/register.html", context={"form":form})

    form = NewUserForm()
    return render (request=request, template_name="user/register.html", context={"form":form})


@login_required
def view_members(request):
    return render(request, 'user/view_members.html', {'data':CustomUser.objects.all()})


@login_required
def update_user_admin(request, id):
    if request.user.is_admin or request.user.is_staff:
        instance = get_object_or_404(CustomUser, id=id)
        form = UpdateUserFormAdmin(request.POST or None, request.FILES or None, instance=instance)
        if request.method == "POST":
            if form.is_valid:
                form.save()
                return redirect("view_members")
            else:
                pass
    else:
        return redirect('index')
    return render(request, "user/update.html", {'form':form})
        

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
            return render(request=request, template_name="user/login.html", context={"form":form})
            
    form = AuthenticationForm()
    return render(request=request, template_name="user/login.html", context={"form":form})


@login_required
def logout_request(request):
	logout(request)
	return redirect("index")


def view_card(request,id):
    instance = get_object_or_404(CustomUser, id=id)
    return render(request, "print_card.html", {'data':instance})


@login_required
def delete_user(request, id):
    if request.user.is_staff or request.user.is_admin:
        instance = get_object_or_404(CustomUser, id=id)
        instance.delete()
    return redirect("view_members")
    
    
@login_required
def profile(request):
    instance = get_object_or_404(CustomUser, id=request.user.id)
    form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=instance)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('dashbord')
    
    return render(request, 'user/profile.html', {'form':form})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
@csrf_exempt
def ajax_fun(request):
    if request.is_ajax() and request.POST['action']=="contact":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        if name!='' or email!='':
            cont = Contact(name=name, email=email, message=message)
            cont.save()
            return JsonResponse({"status": True})
        else:
            pass
    
    
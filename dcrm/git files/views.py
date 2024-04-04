from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    #login 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            messages.success(request,"You have been Logged In!")
            return redirect('home')
        else:
            messages.error(request,"There was an Error Logging In Please try again! ")

    else:

         return render(request,'home.html',{})

#lFor Future Use If required
def login_user(request):
    pass 


def logout_user(request):
   logout(request) 
   messages.success(request,"You have been logged out...")
   return redirect('home')




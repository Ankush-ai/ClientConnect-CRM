from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record


#solved views problems 
# Create your views here.
def home(request):

    records= Record.objects.all()
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

         return render(request,'home.html',{'records':records})

#lFor Future Use If required
def login_user(request):
    pass 


def logout_user(request):
   logout(request) 
   messages.success(request,"You have been logged out...")
   return redirect('home')


def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(usrname=username,password=password)
            login(request,user)
            messages.success(request,"You have been successfully registered!Welcome!")
            return redirect('home')
        

    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')
     
def delete_record(request,pk):
     if request.user.is_authenticated:
          delete_it=Record.objects.get(id=pk)
          delete_it.delete()
          messages.success(request,"Record Deleted Successfully..")
          return redirect('home')
     else:
          messages.success(request,"You must be logged In to delete ...")
          return redirect('home')
     
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
     
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')



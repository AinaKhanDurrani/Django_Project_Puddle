from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from item.models import Category,Item
from .forms import SingupForm

# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:10]
    categories=Category.objects.all()
    context={
        'items':items,
        'categories':categories
    }
    return render(request,'core/index.html',context)

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:index') 
    else:
        form = SingupForm()
    
    context={'form':form}
    return render(request,"core/signup.html",context)

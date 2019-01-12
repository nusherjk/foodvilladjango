from django.shortcuts import render
from .forms import RegisterForm,LoginForm, ComplaintForm
from .models import User, FoodData,Complaints
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
# fix loginverify & createuser


def index(request):
    return render(request, 'v2/home.html')

def login(request):
    form = LoginForm()
    return render(request, 'v2/login.html', {'form':form})

def register(request):
    form = RegisterForm()
    return render(request, 'v2/register.html' , {'form':form})

def contactonaction(request):
    form = ComplaintForm(request.POST)
    if form.is_valid():
        fullname = form.cleaned_data['fullname']
        email = form.cleaned_data['email']
        comment = form.cleaned_data['comment']

        s = Complaints(full_name=fullname,email=email,complain=comment)
        s.save()
    return HttpResponseRedirect('/contactus')

def contact(request):
    form = ComplaintForm()
    return render(request, 'v2/contactus.html', {'form':form})

def about(request):
    return render(request, 'v2/about.html')

def loginverify(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        s  = User.objects.get(email=username)
        if(s.password == password):
            request.session['User.id'] = s.id
            return testu(request,s.id)
        else:
            return HttpResponse('<h1>Username of password doesnt match</h1>')


def logout(request):
    try:
        del request.session['User.id']
    except KeyError:
        return HttpResponse('<h1>Could not log out please try again </h1>')
    return HttpResponseRedirect('/login')




def createuser(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        address = form.cleaned_data['address']
        s = User(first_name=first_name,last_name=last_name,email=email,password=password,address=address)
        s.save()
        return HttpResponse('<h1>account created successfully</h1>')

def testu(request,uid):
    userdata = User.objects.get(id=uid)
    return render(request, 'v2/user.html', context={'data':userdata})

def show(request):
    s = FoodData.objects.all()
    context = {'fooddata': s}
    return render(request, 'v2/foods.html' ,context=context)

def orderview(request):
    burgers = FoodData.objects.filter(category="Burger")
    cakes = FoodData.objects.filter(category="Cake")
    pizzas = FoodData.objects.filter(category="Pizza")
    beverages = FoodData.objects.filter(category="Beverage")
    context = {'burgers': burgers,
               'cakes':cakes,
               'pizzas':pizzas,
               'beverages':beverages
               }
    return render(request,'v2/Order.html', context=context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_view(request):
    return render(request,'testapp/java.html')


@login_required
def python_view(request):
    return render(request,'testapp/python.html')

def logout_view(request):
    return render(request,'testapp/logout.html')
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    title ='Home'

    return render(request,'gallery/home.html')
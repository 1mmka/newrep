from django.shortcuts import render
from app.models import Username

# Create your views here.
def index(request):
    return render(request,'index.html',{'users' : Username.objects.all()})
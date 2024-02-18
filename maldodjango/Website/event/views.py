from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def home(request):
#     Oldies_Day = Oldies_Day.objects.all()
#     workers_day = workers_day.objects.all()
#     Culture_Day = Culture_Day.objects.all()
#     prom = prom.objects.all()
#     Graduation = Graduation.objects.all()
#     Event = Event.objects.all()
#     data = {
#     'old':Oldies_Day,
#     'work':workers_day,
#     'culture':Culture_Day,
#     'prom':prom,
#     'grad':Graduation,
#     'event':Event,
# }
    return render(request,'home.html')
def about_us(request):
    return render(request,'about_us.html')



def experience(request):
     Oldies = Oldies_Day.objects.all()
     workers = workers_day.objects.all()
     Culture = Culture_Day.objects.all()
     pr = prom.objects.all()
     Grad = Graduation.objects.all()
     Exp= Expriance.objects.all()
     data ={
    'old':Oldies,
    'work':workers,
    'culture':Culture,
    'prom':pr,
    'grad':Grad,
    'Expriance':Exp,
}
     return render(request,'experience.html',data)

def future(request):
    return render(request,'future.html')
def contact_us(request):
 return render(request,'contact_us.html')

def oldies(request):
    return render(request,'oldies.html')
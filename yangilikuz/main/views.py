from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Yangiliklar, Info, Dunyo, Texnologiya, yangilikuz


# Create your views here.

def asosiy(request):
   news = Yangiliklar.objects.all()
   contex = {
         'kalitsoz' :news
   }
   return render(request, 'main/index.html', contex)

def dunyo(request):
   foreignnews = Dunyo.objects.all()
   contex = {
         'foreignnews' : foreignnews
   }
   return render(request, 'main/Dunyo.html', contex)

def ozbekiston(request):
   news = Yangiliklar.objects.all()
   contex = {
         'kalitsoz' :news
   }
   return render(request, 'main/index.html', contex)

def texnologiya(request):
   texnikalar = Texnologiya.objects.all()
   ozgaruvchi = {
         'texnologiya' : texnikalar
   }
   return render(request, 'main/Texnologiya.html', ozgaruvchi)

def about(request):
    infos = Info.objects.all()
    ozgaruvchi ={
        # malumotlarni viewsdan templatega uztish uchun
        'kalitsoz': infos

    }
    return render(request,'main/about.html', ozgaruvchi)

def newsuz(request):
   news = yangilikuz.objects.all()
   contex = {
         'kalitsoz' : news
   }
   return render(request, 'main/yangilikuz.html', contex)


from django.urls import path
from .views import asosiy, dunyo, ozbekiston, texnologiya, about, newsuz

urlpatterns = [
    path('', asosiy, name='main'), # yangi.uz
    path('dunyo', dunyo, name='dunyo'), # yangi.uz/about
    path('uzbekistan', ozbekiston, name='ozbekiston'),
    path('texnologiya', texnologiya, name='texnologiya'),
    path('about', about, name='biz_haqimizda'),
    path('yangilikuz', newsuz, name='yangilik')
]

from django.contrib import admin
from .models import Yangiliklar, Info, Dunyo, Texnologiya, yangilikuz
# Register your models here.

admin.site.register(Yangiliklar),
admin.site.register(Info),
admin.site.register(Dunyo),
admin.site.register(Texnologiya),
admin.site.register(yangilikuz)
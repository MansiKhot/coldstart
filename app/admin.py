from django.contrib import admin
from .models import Users, Ratings, Movies,Info

# Register your models here.


admin.site.register(Users)
admin.site.register(Ratings)
admin.site.register(Movies)
admin.site.register(Info)
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('movie_disp/',views.movie_disp,name='movie_disp'),
    path('register/',views.reg,name='register'),
    path('addreview/',views.add_review,name='add-review'),
    path('a/',views.import_db,name='importdb'),
    path('h/',views.products_list,name='h'),
    path('h/movies/<slug:id>',views.movies,name='movie'),
    #path('items/',views.items,name='items'),
    path('d/',views.createdata,name='d'),
    path('done/',views.done,name='done'),
    path('forms/',views.forms,name='forms'),
    path('newuser/',views.newuser,name='newuser'),
]
from django.shortcuts import render
from django.db import models
from .models import Users,Movies,Ratings,Info
from django.views.generic import ListView
from . import predictor
#from . import uform 
from .forms import NameForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


def movie_disp(request):
    return render(request, 'movie_disp.html')


def reg(request):
    return render(request, 'register.html')


def add_review(request):
    return render(request, 'add_review.html')

def m(request):
    return render(request, 'm.html')

def done(request):
    return render(request, 'done.html')

# def forms(request):
#     if request.method == "GET":
#         form = Uform(request.GET)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('userid', pk=post.pk)
#         else:
#             form = Uform()
#         return render(request, 'userid.html', {'form': form})

# def items(request):
#     return render(request, 'items.html')

def forms(request):
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
    # check whether it's valid:
        if form.is_valid():
        # process the data in form.cleaned_data as required

        # ...
        # redirect to a new URL:
            return generate_pdf(request, Type_id)

# if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()

        return render(request, 'film/userid.html', {'form': form, 'type_id': Type_id})

def import_db(request):
    
    f = open('C:/sh-master/movies/film/u.csv', 'r')  
    for line in f:
        line =  line.split('|')
        print(line)
        tmp = Movies(
            movie_id = int(line[0].replace('"','')),
            movie_title = line[1],
            #release_date = line[2],
            #video_release_date = line[3],
            Imdb_url = line[4],
            unknown = line[5],
            action = line[6],
            adventure = line[7],
            animation = line[8],
            children = line[9],
            comedy = line[10],
            crime =line[11],
            documentary = line[12],
            fantasy = line[13],
            film_noir = line[14],
            horror = line[15],
            musical = line[16],
            mystery = line[17],
            romance = line[18],
            sci_fi = line[19],
            thriller =line[20],
            war = line[21],
            western = line[22]
              
        )
        tmp.save()

    f.close()

    
class IndexView(ListView):
    template_name = 'post/m.html'

    def get_queryset(self):
        return Movies.objects.all()

def products_list(request):
    products = Movies.objects.all()[0:10]
    #print(products)
    return render(request, 'h.html',
                  context={'product_list': products})

def createdata(request):
        if request.method == 'GET':
            if request.GET.get('username') and request.GET.get('name') and request.GET.get('email') and request.GET.get('password'):
                post=Info()
                post.username= request.GET.get('username')
                post.name= request.GET.get('name')
                post.email= request.GET.get('email')
                post.password= request.GET.get('password')
                #post.newage= request.GET.get('newage')
                # post.newsex= request.GET.get('newsex')
                # post.newoccupation= request.GET.get('newoccupation') 
                post.save()
                
                return render(request, 'demo.html')  

        else:
                return render(request,'demo.html')


def movies(request,id):
    x = predictor.similarityPredictionItem(predictor.item_similarity)
    print()
    listed = []
    listed = x[id]
    m = []
    print(listed)
    for i in listed:
        m.append(predictor.items.loc[i-1]['movie_title'])
    return render(request, 'items.html', context={'movies': m})

def users(request,id):
    x = predictor.similarityPrediction(predictor.user_similarity)
    print()
    listed = []
    listed = x[id]
    m = []
    print(listed)
    for i in listed:
        m.append(predictor.items.loc[i-1]['movie_title'])
    return render(request, 'userid.html', context={'users': m})

def newuser(request):
        if request.method == 'GET':
            if request.GET.get('age')and request.GET.get('sex')and request.GET.get('occupation'):
                post=Info()
                
                post.age= request.GET.get('age')
                post.sex= request.GET.get('sex')
                post.occupation= request.GET.get('occupation') 
                post.save()
                
                return render(request, 'done.html')  

        else:
                return render(request,'done.html') 

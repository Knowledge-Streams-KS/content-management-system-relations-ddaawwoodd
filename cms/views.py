from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *


def createarticle(request):

    if request.method == "POST":

        title = request.POST.get('title')
        content = request.POST.get('content')
        publication_date = request.POST.get('publication_date')

        categ = request.POST.get('categories')
        categories = Categories.objects.filter(name=categ)

        auth= request.POST.get('author')
        author = User.objects.filter(name=auth)


        new_article = Articles.objects.create(title=title, content=content, 
            publication_date=publication_date, author=author)
        
        new_article.categories.set(categories)

        return render(request, "homepage.html")
    
    else:
        categories = Categories.objects.all()
        users = User.objects.all()
        return render(request, "article.html", {"categories":categories, "users":users})


    

def createcategory(request):

    if request.method == "POST":

        name = request.POST.get("name")

        new_category = Categories.objects.create(name=name)
        return HttpResponse("category is created")
    
    else:
        return render(request, "category.html")
    

def homepage(request):
    articles = Articles.objects.all()
    return render(request, 'homepage.html', {'articles':articles})


def article_detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'article_detail.html', {'article': article})



from django.urls import path 
from cms import views

urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path("createarticle/", views.createarticle, name="create_article"),
    path("createcategory/", views.createcategory, name="create_category"),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]

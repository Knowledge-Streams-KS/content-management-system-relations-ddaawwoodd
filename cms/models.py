from django.db import models

class User(models.Model):

    username = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)


class Categories(models.Model):

    name = models.CharField(max_length=64)


class Articles(models.Model):

    title = models.CharField(max_length = 64)
    content = models.TextField()
    publication_date = models.DateField()
    categories = models.ManyToManyField(Categories)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
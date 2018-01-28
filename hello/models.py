from django.db import models

# Create your models here.

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

class Author(models.Model):
	name = models.CharField(max_length=30)

class AuthorDetail(models.Model):
	sex = models.BooleanField(max_length=1, choices=((0, 'M'),(1, 'F'),))	
	email = models.EmailField()
	birthday = models.DateField()
	author = models.OneToOneField(Author, on_delete=models.CASCADE,)

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date = models.DateField()
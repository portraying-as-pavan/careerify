from django.db import models
from django.contrib.auth.models import User
# Create your models here.

type_options=(
	("1","on-campus"),
	("2","PPO"),
	("3","off-campus"),
	)
branch_options=(
	("1","core"),
	("2","non-core"),
	)

class Post(models.Model):
	name=models.CharField(max_length=200)
	photo = models.ImageField(upload_to='images/',default='/images/default.jpeg')
	company=models.CharField(max_length=200)
	year=models.CharField(max_length=20)
	type_of_place=models.CharField(max_length=20,
		choices=type_options,
		default="1")
	branch=models.CharField(max_length=10,
		choices=branch_options,
		default="1")
	title=models.CharField(max_length=200)
	content = models.TextField()
	updated_on = models.DateTimeField(auto_now= True)
	created_on = models.DateTimeField(auto_now_add=True)
	#slug = models.SlugField(max_length=200, unique=True)

class Meta:
	ordering = ['-created_on']

def __str__(self):
	return self.title        
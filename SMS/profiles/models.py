from django.db import models
from django.contrib.auth.models import User
from .utils import get_random_code
from django.template.defaultfilters import slugify

# Create your models here.


class Profile(models.Model):

	class Level(models.IntegerChoices):
		Sleepy_baby  = 0
		Basic_Teen = 1
		Average_Nerd = 2
		Script_Kiddie = 3
		Hacker = 4
		Master = 5

	

	## BASE ##

	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	
	email = models.EmailField(max_length=200)
	avatar = models.ImageField(default='chicken.jpg', upload_to='avatars/')
	info = models.TextField(max_length=200, default='N\A')
	username = models.CharField(max_length=200, default='#user')

	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)

	## END_BASE ##

	## ACTIVITY / STATS ##

	XP = models.IntegerField(default=0)
	level = models.IntegerField(choices=Level.choices,default=0)
	global_rank = models.IntegerField(default=0)
	puzzles_completed = models.IntegerField(default=0)
	courses_completed = models.IntegerField(default=0)
	languages = models.TextField(max_length=100, default='N\A')
	

	## END_ACTIVITY / END_STATS ##

	@property
	def user__username(self):
		return self.user.username
		
	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return f"{self.user.username}--{self.created}"

	

	
	
	
	






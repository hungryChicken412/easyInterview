from django.contrib.auth.models import User
from django.db import models

from autoslug import AutoSlugField
import sys
sys.path.append('..')
from profiles.models import Profile


# Create your models here.




class Question(models.Model):
	questionType = models.CharField(max_length=50, default='number')
	marks = models.IntegerField(default=1)
	description = models.TextField(default='')

	answer = models.CharField(max_length=50, default=0)

	choice_a = models.CharField(max_length=200, default='a')
	choice_b = models.CharField(max_length=200, default='b')
	choice_c = models.CharField(max_length=200, default='c')
	choice_d = models.CharField(max_length=200, default='d')

	slug = AutoSlugField(populate_from='description')


	def __str__(self):
		return self.questionType+self.slug


class Interview(models.Model):

	interview_name = models.CharField(max_length=200)
	description = models.TextField()
	passingMarks = models.IntegerField(default=22)
	endDate = models.DateTimeField()
	slug = AutoSlugField(populate_from='interview_name')

	questions = models.ManyToManyField(Question, related_name="Questions")

	def __str__(self):
		return self.interview_name

class AnswerQuestion(models.Model):
	question = models.ForeignKey(Question, on_delete=models.PROTECT, blank=True)
	user_answer = models.CharField(max_length=200)


class InterviewSolution(models.Model):

	email = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	resume = models.FileField(upload_to='resumes/')
	interview = models.ForeignKey(Interview, on_delete=models.CASCADE)

	marks = models.IntegerField(default=0)

	correct = models.ManyToManyField(AnswerQuestion, related_name="Incorrect", blank=True)

	incorrect = models.ManyToManyField(AnswerQuestion, related_name="Correct", blank=True)

	def __str__(self):
		return self.interview.interview_name + 'solution by ' + self.name







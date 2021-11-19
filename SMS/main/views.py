from django.shortcuts import render

from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from django.contrib.auth.models import User
from django.db.models.aggregates import Max

from .serializers import InterviewSerializer, InterviewSolutionSerializer, QuestionSerializer
from .models import Interview, InterviewSolution

# Create your views here.
# ViewSets define the view behavior.



class InterviewViewSet(viewsets.ModelViewSet):
	serializer_class = InterviewSerializer

	def get_queryset(self):
		name = self.kwargs.get('slug')
		data = Interview.objects.get(slug=name)

		print(data.questions)

		return [data]
		
class questionViewSet(viewsets.ModelViewSet):
	serializer_class = QuestionSerializer(many=True)

	def get_queryset(self, many=True):
		name = self.kwargs.get('slug')
		data = Interview.objects.get(slug=name)

		return [data]

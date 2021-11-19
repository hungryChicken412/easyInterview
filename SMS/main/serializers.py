from django.db.models import fields
from rest_framework import serializers, viewsets
from .models import Interview, InterviewSolution, Question



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('questionType', 'marks', 'description','choice_a', 'choice_b', 'choice_c', 'choice_d')
    



class InterviewSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)
    class Meta:
        model = Interview
        fields = ('interview_name', 'description', 'passingMarks', 'endDate', 'questions')
   



class InterviewSolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewSolution
        fields = ('email', 'name', 'resume', 'interview', 'marks', 'correct', 'incorrect')
    


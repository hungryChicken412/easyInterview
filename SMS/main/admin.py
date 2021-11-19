from django.contrib import admin
from .models import Question, Interview, InterviewSolution, AnswerQuestion
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

admin.site.register(InterviewSolution)
admin.site.register(AnswerQuestion)

admin.site.register(Interview)
admin.site.register(Question)



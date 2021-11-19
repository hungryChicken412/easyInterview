from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import PuzzleSolution, Puzzle


class SolutionForm(forms.Form):
	solution = forms.Textarea()
    
	class Meta:
		model = PuzzleSolution
		fields = ("username")
	def save(self, commit=True):
		user = super(SolutionForm, self).save(commit=False)
		user.content = self.cleaned_data['solution']

		if (commit):
			user.save()

		return user
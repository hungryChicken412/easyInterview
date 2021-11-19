
from main.models import Interview
from django.shortcuts import render
from .models import Profile
from .forms import ProfileModelForm
from .serializers import ProfileSerializer, HighscoreSerializer
from rest_framework import routers, serializers, viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.views import APIView

import sys
sys.path.append('..')

# Create your views here.


def my_profile_view(request):
	profile = Profile.objects.get(user=request.user)
	form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
	confirm = False

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			confirm = True

	context = {
		'profile' : profile,
		'form': form,
		'confirm': confirm,
	}

	return render(request, 'profiles/myprofile.html', context)



# Create your views here.
# ViewSets define the view behavior.

class ProfileViewSet(viewsets.ModelViewSet):
	serializer_class = ProfileSerializer
	
	def get_queryset(self):
		name = self.kwargs.get('username')
		if (name == 'me'):
			name = self.request.user.username
		else:
			pass
			
		profile = Profile.objects.filter(username=name)
		return profile

	authenticationClasses = (TokenAuthentication,)
	permissionClasses = (IsAuthenticated,)


class EditUserViewSet(viewsets.ModelViewSet):
	serializer_class = HighscoreSerializer
	def get_queryset(self):
		users = Profile.objects.all().order_by('XP')
		return users[::-1]
	def put(self, request, *args, **kwargs):
		
		user = Profile.objects.get(user=self.request.user)
		error = "NONE"
		change = "NONE"
		if (len(self.request.data) == 2):
			try:
				info = self.request.data['info']
				languages = self.request.data['languages']
				user.info = info
				user.languages = languages
				user.save()
				change = "CHANGES"
			except Exception as e:
				
				error = str(e)
				
		
		returnData = {'username':user.username,'info': user.info, 'languages':user.languages, 'ERROR':error, 'CHANGE':change}
		return Response(returnData)


    
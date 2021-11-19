from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Interview
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from .api.Tio import Tio



host = ""
app= "https://localhost:4200"
"""

def singleSlug(request, single_slug):
	site = Tio()

	if (request.method == "POST"):
		try:
			solve = request.POST.get("solutionCode")
			puzzleInstance = Puzzle.objects.get(puzzle_slug=single_slug)
			print(solve)
			tioReq = site.new_request('python3', solve)
			tioResponce = site.send(tioReq).split("\n")[0]

			if (tioResponce == puzzleInstance.answer):
				messages.success(request,  tioResponce)
				solution = PuzzleSolution(user=request.user, puzzle=puzzleInstance, content=solve)
				solution.save()
			else:
				messages.success(request,  "WRONG!")
		except:
			messages.success(request,  "Something Went Wrong!")
		




	categories = [c.category_slug for c in Difficulty.objects.all()]
	if (single_slug in categories):
		matching_puzzles = Puzzle.objects.filter(puzzle_category__category_slug=single_slug)
		series_url = {}

		for m in matching_puzzles.all():
			series_url[m] = m.puzzle_slug

		

		context = {
			'part_ones': series_url,
			
		}
		return render(request, "main/category.html", context)
	
	course = [c.puzzle_slug for c in Puzzle.objects.all()]

	if (single_slug in course):

		this_course = Puzzle.objects.get(puzzle_slug=single_slug)
        

		context = {
			"course" : this_course,


		}
		return render(request, "main/course.html", context)

	return HttpResponse(f"{single_slug} does not correspond to anything.")

"""

def landing(request):
	# return HttpResponse('Hello World')
	user = request.user
	hello = 'hello world'
	context = {
		'user':user,
		'hello':hello,
		'categories': Interview.objects.all,
	}
	return render(request, 'landing.html', context)


def home_view(request):
	# return HttpResponse('Hello World')
	user = request.user
	hello = 'hello world'
	context = {
		'user':user,
		'hello':hello,
		'categories': Interview.objects.all,
	}
	return render(request, 'main/categories.html', context)




def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,  f"New Account Created: {username}")
			login(request, user)
			messages.info(request,  f"You are now logged in as {username}")
			return redirect(app + '/login/')
		else:
			for msg in form.error_messages:
				messages.error(request, f"Something Went Wrong! Password Don't Match or Username/Email already Exists!")

	


	form = NewUserForm
	context = {
		'form': form,
	}

        
	if request.user.is_authenticated:
		return redirect(app + '/login/')
	else:
		return render(request, 'main/register.html', context )
	


def logout_request(request):
	logout(request)
	messages.info(request, f"Logged Out Successfully!")
	return redirect(host + '/')

def login_request(request):
        
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if (user is not None):
				login(request, user)
				messages.info(request,  f"You are now logged in as {username}")
				return redirect(host + '/app/')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")



	form = AuthenticationForm()
	context = {
		"form": form,
	}
	if request.user.is_authenticated:
		return redirect(host + '/app/')
	else:
		return render(request, "main/login.html", context)

	

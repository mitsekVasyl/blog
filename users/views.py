from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	""" Register new user """
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		# Process form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# login and redirect to home
			login(request, new_user)
			return redirect('blogs:blogposts')

	context = {'form': form}
	return render(request, 'users/register.html', context)
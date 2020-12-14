from django.shortcuts import render, redirect, get_objects_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404


from .models import BlogPost
from .forms import PostForm

def blogposts(request):
	""" Display topic """
	blogposts = BlogPost.objects.order_by('date_added')
	context = {'blogposts': blogposts}
	return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
	""" Adding new post """
	if request.method != 'POST':
		# Empty
		form = PostForm()
	else:
		# POST
		form = PostForm(data=request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.owner = request.user
			new_post.save()
			return redirect('blogs:blogposts')
	
	context = {'form': form}
	return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
	""" Edit existing post """
	post = get_objects_or_404(BlogPost, id=post_id)
	# Ensure user is owner
	if post.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# Fills form by data of current post
		form = PostForm(instance=post)
	else:
		form = PostForm(instance=post, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('blogs:blogposts')

	context = {'post': post, 'form': form}
	return render(request, 'blogs/edit_post.html', context)
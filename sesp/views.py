from django.shortcuts import render
from django.utils import timezone
from .models import Post
def homes(request):
	posts = Post.objects.all
	return render(request, 'sesp/homes.html', {'posts':posts})

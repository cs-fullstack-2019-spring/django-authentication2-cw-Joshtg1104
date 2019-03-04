from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required


# Create your views here.
# renders the login page
def index(request):
    return render(request, 'blogApp/index.html')

# Filters out blog entries/context based on the login
@login_required
def blogPosts(request):
    entries = Blog.objects.filter(blog_key=request.user)
    context = {
        "entries": entries
    }
    return render(request, 'blogApp/blogPosts.html', context)

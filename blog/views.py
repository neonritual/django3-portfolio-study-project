from django.shortcuts import render, get_object_or_404
from .models import Blogs



def all_blogs(request):
    blog = Blogs.objects.order_by('-created_date')[:5]
    return render(request, 'blog/all_blogs.html', {'blog':blog})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'blogs':blog})

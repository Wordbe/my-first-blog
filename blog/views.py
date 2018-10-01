from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# from djangogirls.blog.models import Post
# from djangogirls.blog.forms import PostForm

# def post_list(request):
#    return render(request, 'blog/post_list.html', {})
def base(request):
     return render(request, 'blog/base.html', {})

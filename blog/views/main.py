from django.shortcuts import render
# from django.utils import timezone
# from ..models import Post

def main(request):
    return render(request, 'blog/main.html', {})

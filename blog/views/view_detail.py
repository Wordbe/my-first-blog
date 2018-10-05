from django.shortcuts import render

def detail(request):
    return render(request, 'blog/detail.html', {})

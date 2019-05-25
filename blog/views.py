from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'Blog 1 content',
        'date_posted': 'May 31 2019'
    },
    {
        'author': 'Chinnam',
        'title': 'Blog Post 2',
        'content': 'Blog post 2 content',
        'date_posted': 'June 1 2019'
    }

]

def home(request):
    context = {
        'posts': posts,
        'title': 'Title'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

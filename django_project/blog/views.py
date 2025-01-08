from django.shortcuts import render

posts = [
    {
        'author' : 'Barbare',
        'title' : 'BlogPost 1',
        'content' : 'First Post',
        'date_posted' : 'January 8, 2024'
    },
    {
        'author': 'Nino',
        'title': 'BlogPost 2',
        'content': 'Second Post',
        'date_posted': 'January 9, 2024'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')


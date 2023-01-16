from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group


NUMBER_OF_POSTS = 10
def index(request):
    posts = Post.objects.order_by('-pub_date')[:NUMBER_OF_POSTS]
    context = {
        'posts': posts,
        'title': 'Последние обновления на сайте',
        'text': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUMBER_OF_POSTS]
    context = {
        'group' : group,
        'posts' : posts,
    }
    return render(request, 'posts/group_list.html', context)







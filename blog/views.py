from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Post

def index(request):
    # return HttpResponse("Blog : page d'accueil..")

    posts_list = Post.objects.order_by('-pub_date')
    # return HttpResponse(posts_list)

    model = {'posts_list': posts_list}
    return render(request, 'blog/index.html', model)

def detail(request, post_id):
    # return HttpResponse("Blog : détail post num %s.." % post_id)

    # try:
    #     post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     raise Http404("Post introuvable!")

    # utilisation de get_object_or_404 :
    post = get_object_or_404(Post, pk=post_id)
 
    return render(request, 'blog/detail.html', {'post': post})

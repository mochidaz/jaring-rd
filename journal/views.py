from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category


def home(request):
    featured_post = Post.objects.filter(is_featured=True).order_by('-created_at').first()

    if featured_post:
        latest_posts = Post.objects.exclude(pk=featured_post.pk, is_draft=True).order_by('-created_at')[:3]
    else:
        latest_posts = Post.objects.filter(is_draft=False).order_by('-created_at')[:3]

    return render(request, 'journal/home.html', {
        'latest_posts': latest_posts,
        'featured_post': featured_post
    })


def post_list(request):
    category_slug = request.GET.get('cat')
    search_query = request.GET.get('q')

    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    if category_slug:
        posts = posts.filter(category__slug=category_slug, is_draft=False)

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query),
            is_draft=False
        )

    context = {
        'posts': posts,
        'categories': categories,
        'current_cat': category_slug,
        'search_query': search_query
    }
    return render(request, 'journal/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'journal/post_detail.html', {'post': post})
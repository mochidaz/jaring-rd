from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from about.models import Circle
from journal.models import Post, Category
from .forms import PostForm, CircleForm, CategoryForm


@staff_member_required
def dashboard_home(request):
    post_count = Post.objects.count()
    circle_count = Circle.objects.count()
    category_count = Category.objects.count()
    latest_posts = Post.objects.order_by('-created_at')[:5]

    return render(request, 'dashboard/index.html', {
        'post_count': post_count,
        'circle_count': circle_count,
        'category_count': category_count,
        'latest_posts': latest_posts
    })


@staff_member_required
def category_list(request):
    search_query = request.GET.get('q', '')
    sort_param = request.GET.get('sort', 'name')

    categories = Category.objects.all()

    if search_query:
        categories = categories.filter(name__icontains=search_query)

    valid_sorts = ['name', '-name', 'slug', '-slug']
    if sort_param in valid_sorts:
        categories = categories.order_by(sort_param)
    else:
        categories = categories.order_by('name')

    return render(request, 'dashboard/category_list.html', {
        'categories': categories,
        'search_query': search_query,
        'current_sort': sort_param
    })


@staff_member_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kategori baru ditambahkan.")
            return redirect('dashboard:category_list')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Tambah Kategori'})


@staff_member_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Kategori diperbarui.")
            return redirect('dashboard:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Edit Kategori'})


@staff_member_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.warning(request, "Kategori dihapus.")
    return redirect('dashboard:category_list')


@staff_member_required
def post_list(request):
    search_query = request.GET.get('q', '')
    sort_param = request.GET.get('sort', '-created_at')

    posts = Post.objects.all()

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query)
        )

    valid_sorts = ['title', '-title', 'category__name', '-category__name', 'created_at', '-created_at', 'author',
                   '-author']
    if sort_param in valid_sorts:
        posts = posts.order_by(sort_param)
    else:
        posts = posts.order_by('-created_at')

    return render(request, 'dashboard/post_list.html', {
        'posts': posts,
        'search_query': search_query,
        'current_sort': sort_param
    })


@staff_member_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.save()
            messages.success(request, "Manuskrip berhasil ditambahkan.")
            return redirect('dashboard:post_list')
    else:
        form = PostForm()
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Tulis Jurnal Baru'})


@staff_member_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Manuskrip diperbarui.")
            return redirect('dashboard:post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Edit Jurnal'})


@staff_member_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.warning(request, "Manuskrip telah dibakar (dihapus).")
    return redirect('dashboard:post_list')


@staff_member_required
def circle_list(request):
    search_query = request.GET.get('q', '')
    sort_param = request.GET.get('sort', 'name')

    circles = Circle.objects.all()

    if search_query:
        circles = circles.filter(
            Q(name__icontains=search_query) |
            Q(genre__icontains=search_query) |
            Q(master__icontains=search_query)
        )

    valid_sorts = ['name', '-name', 'genre', '-genre', 'master', '-master', 'est_year', '-est_year']
    if sort_param in valid_sorts:
        circles = circles.order_by(sort_param)
    else:
        circles = circles.order_by('name')

    return render(request, 'dashboard/circle_list.html', {
        'circles': circles,
        'search_query': search_query,
        'current_sort': sort_param
    })


@staff_member_required
def circle_create(request):
    if request.method == 'POST':
        form = CircleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Circle baru terdaftar.")
            return redirect('dashboard:circle_list')
    else:
        form = CircleForm()
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Tambah Circle'})


@staff_member_required
def circle_edit(request, pk):
    circle = get_object_or_404(Circle, pk=pk)
    if request.method == 'POST':
        form = CircleForm(request.POST, request.FILES, instance=circle)
        if form.is_valid():
            form.save()
            return redirect('dashboard:circle_list')
    else:
        form = CircleForm(instance=circle)
    return render(request, 'dashboard/form.html', {'form': form, 'title': 'Edit Circle'})


@staff_member_required
def circle_delete(request, pk):
    circle = get_object_or_404(Circle, pk=pk)
    circle.delete()
    return redirect('dashboard:circle_list')

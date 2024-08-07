from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Vista para el blog
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

# Vista para una categoría específica
def category(request, category_id):
    category_instance = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category_instance)  # Usar 'categories'
    return render(request, 'blog/category.html', {'category': category_instance})

from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'titulo': 'Blog'
        }
        posts = Post.objects.all()
        context['posts'] = posts
        return render(request, 'blog/blog_list.html', context)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        context = {
            'titulo': 'Crear articulo',
            'form': form
        }
        return render(request, 'blog/blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                p, created = Post.objects.get_or_create(title=title, 
                                                        defaults={'content': content})
                try:
                    p.save()
                except Exception as e:
                    form.add_error('title', 'El articulo ya existe')
                if created:
                    return redirect('blog:blog_list')
                else:
                    form.add_error('title', 'El articulo ya existe')
        else:
            form = PostForm()
        context = {
            'titulo': 'Crear articulo',
            'form': form
        }

        return render(request, 'blog/blog_create.html', context)

class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }

        return render(request, 'blog/blog_detail.html', context)


class BlogUpdateView(View):
    """
    Vista para actualizar un articulo
    """
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        context = {
            'titulo': 'Actualizar articulo',
            'form': form
        }
        return render(request, 'blog/blog_update.html', context)

    def post(self, request, pk, *args, **kwargs):
        """
        Vista para actualizar un articulo
        """
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_list')
        context = {
            'titulo': 'Actualizar articulo',
            'form': form
        }
        return render(request, 'blog/blog_update.html', context)

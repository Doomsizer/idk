from datetime import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .filters import PostFilter
from .forms import PostForm, CategoryForm, AuthorForm
from .models import Post, Author, Category


class Posts(ListView):
    model = Post
    ordering = '-time_created'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context


class PostCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('simpleapp.add_post')
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class AuthorCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_author')
    form_class = AuthorForm
    model = Author
    template_name = 'post_edit.html'


class CategoryCreate(PermissionRequiredMixin,CreateView):
    permission_required = ('simpleapp.add_category')
    form_class = CategoryForm
    model = Category
    template_name = 'post_edit.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.add_post')
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_post')
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')

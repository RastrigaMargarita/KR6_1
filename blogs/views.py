from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blogs.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'published')
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'published')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_detail', args=[self.kwargs.get('slug')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_number += 1
        self.object.save()
        return self.object
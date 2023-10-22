from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        if self.object.views_count == 100:
            send_mail(
                'Поздравляем!',
                f'Поздравляем! Ваш блог "{self.object.title}" просмотрели 100 раз!',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER]
            )
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        from django.urls import reverse
        return reverse('blog:view_blog', args=[self.object.slug])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list_blog')

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Fee
from django.contrib.auth.decorators import login_required


# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27,2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28,2018'
#     }
#
# ]

#

def home(request):
    return render(request, 'blog/home.html')


class PostListView(ListView):
    model = Post
    template_name = 'users/rate.html'
    context_object_name = 'posts'
    ordering = ['-author']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # author set garna lai yo talako
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # author set garna lai yo talako
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/rate'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def rate(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'users/rate.html', context)
    # Create your views  here.


# for account section
@login_required
def account(request):
    return render(request, 'blog/account.html')


class FeeListView(ListView):
    model = Fee
    template_name = 'blog/account-list.html'
    context_object_name = 'fees'
    ordering = ['fullname']

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Fee, Fullfee, Book, AddFee
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


# from users.forms import BookForm


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


@login_required
def document(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'blog/document-section.html', context)


# def book_list(request):
#     books = Book.objects.get(user=request.user)
#     return render(request, 'blog/book_list.html', {'books': books})


class BookList(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'blog/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(is_private=False).order_by('-date')


class BookListPrivate(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Book
    template_name = 'blog/book_list_private.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user).order_by('-date')


# def upload_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'blog/upload_book.html', {'form': form})


class UploadBook(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'blog/upload_book.html'
    # context_object_name = 'book'
    fields = ['title', 'details', 'thumbnail', 'author', 'file', 'year', 'faculty', 'is_private']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'details', 'thumbnail', 'author', 'file', 'year', 'faculty', 'is_private']
    template_name = 'blog/upload_book.html'

    # author set garna lai yo talako
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.user:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/books'
    template_name = 'blog/book_delete.html'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.user:
            return True
        return False


# using class based views
class PostListView(ListView):
    model = Post
    template_name = 'users/rate.html'
    context_object_name = 'posts'
    ordering = ['date']


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


# Add Fee Section For Staffs

class AddFeeCreateView(LoginRequiredMixin, CreateView):
    model = AddFee
    fields = ['name', 'roll_no', 'is_hostel', 'faculty', 'year', 'fees_type', 'fee_month', 'amount']
    template_name = 'blog/AddFee.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddFeeListView(LoginRequiredMixin, ListView):
    model = AddFee
    template_name = 'blog/account-list.html'
    context_object_name = 'fees'
    queryset = AddFee.objects.all()
    ordering = ['-fee_paid_date']


class AddFeeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AddFee
    fields = ['name', 'roll_no', 'is_hostel', 'faculty', 'year', 'fees_type', 'fee_month', 'amount']
    template_name = 'blog/AddFee.html'

    # author set garna lai yo talako
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        fee = self.get_object()
        if self.request.user == fee.user:
            return True
        return False


# Normal User View Fee Transactions

class ViewFeeTrans(LoginRequiredMixin, ListView):
    model = AddFee
    template_name = 'blog/yourtrans.html'
    context_object_name = 'fees'

    def get_queryset(self):
        print(self.request.user.roll_no)
        return AddFee.objects.filter(roll_no=self.request.user.roll_no).order_by('-fee_paid_date')

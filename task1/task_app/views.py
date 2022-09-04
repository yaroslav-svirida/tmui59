from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from task_app.forms import CreatePostForm, RegisterUserForm, LoginUserForm, CreateBookForm
from task_app.models import Post, Book

'''Канареечные записи'''
Honey_pot = ['bird96', 'fly96', 'dog97', 'run97']

def createbook(request):
    form = CreateBookForm(request.POST)
    if request.method == 'POST':

        if not request.user.is_authenticated:
            if Book.objects.filter(text=Honey_pot[0], name=Honey_pot[1], honey_token=1).count() < 2:
                Book.objects.create(text=Honey_pot[0], name=Honey_pot[1], honey_token=1)

        if request.user.is_authenticated:

            if form.is_valid():
                form.save()
            return redirect('show_post')
        else:
            form = CreateBookForm()

    return render(request, 'createbook.html', {'form': form, 'title': 'Create book'})

def createpost(request):
    form = CreatePostForm(request.POST)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            if Post.objects.filter(text=Honey_pot[0], name=Honey_pot[1], honey_token=1).count() < 2:
                Post.objects.create(text=Honey_pot[0], name=Honey_pot[1], honey_token=1)
        if request.user.is_authenticated:

            if form.is_valid():
                form.save()
            return redirect('show_post')
        else:
            form = CreatePostForm()
    return render(request, 'createpost.html', {'form': form, 'title': 'Create post'})

class GetAllPosts(ListView):
    model = Post
    template_name = 'all_posts.html'
    context_object_name = 'topics'



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(honey_token=0)
        return context

# def get_all_posts(request):
#     # admin = User.objects.get(username='admin')
#     # if request.user == admin:
#     #     posts = Post.objects.filter(times_of_edit=1)
#     #     books = Book.objects.filter(honey_token=1)
#     #
#     #
#     # else:
#     # posts = Post.objects.filter(honey_token=0)
#     # books = Book.objects.filter(honey_token=0)
#     posts = Post.objects.all()
#     books = Book.objects.all()
#     context = {
#         'topics': posts,
#         'books': books,
#
#     }
#     return render(request, 'all_posts.html', context)

def get_all_birds(request):

    posts = Post.token_objects.all()
    books = Book.token_objects.all()

    context = {
        'topics': posts,
        'books': books,

    }
    return render(request, 'all_posts.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('create_post')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('show_post')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('show_post')


def logout_user(request):
    logout(request)
    return redirect('login')

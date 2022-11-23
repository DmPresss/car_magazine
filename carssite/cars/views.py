from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView

from . models import Car, Category
from . forms import *


menu = [{'title': "About", 'url_name': 'cars:about'},
        {'title': "Add Post", 'url_name': 'cars:addpost'},
        {'title': "Feedback", 'url_name': 'cars:contact'},
        {'title': "Signin", 'url_name': 'cars:login'}
        ]


class CarIndex(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Car.objects.filter(is_published=True)


def about(request):  # HttpRequest
    context = {
        'title': '!!ABOUT SITE PAGE',
        'menu': menu
    }
    return render(request, 'cars/about.html', context)


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'cars/addpost.html'
    success_url = reverse_lazy('cars:index')

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Adding post'
        return context


def contact(request):
    return HttpResponse('contacts')


def login(request):
    return HttpResponse('login')


class ShowPost(DeleteView):
    model = Car
    template_name = 'cars/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


class CarCategory(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return Car.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>ERROR = 404 , Page is not found</h1>')


# def index(request):  # HttpRequest
#     posts = Car.objects.all()
#     #cats = Category.objects.all()
#     context = {
#         # 'cats': cats,
#         'title': 'THE MAIN PAGE',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': 0,
#     }
#     return render(request, 'cars/index.html', context)


# def show_post(request, post_slug):
#     post = get_object_or_404(Car, slug=post_slug)

#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,

#     }

#     return render(request, 'cars/post.html', context)


# def show_category(request, cat_slug):
#     cat = Category.objects.get(slug=cat_slug)
#     posts = Car.objects.filter(cat_id=cat.id)
#     #cats = Category.objects.all()

#     if len(posts) == 0:
#         raise Http404()

#     context = {
#         # 'cats': cats,
#         'title': cat,
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': cat.id,
#     }
#     return render(request, 'cars/index.html', context)

# def addpost(request):
#     # form = AddPostForm()
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('cars:index')
#     else:
#         form = AddPostForm()
#     context = {
#         'title': 'Adding the post',
#         'menu': menu,
#         'form': form,
#     }
#     return render(request, 'cars/addpost.html', context)

# def cars_models(request, mod):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'<h2>name of cars models={mod}</h2>')

# def year_of_build(request, year):
#     if int(year) > 2020:
#         return redirect ('cars:index', permanent=True)
#     #   raise  Http404()

#     return HttpResponse(f'<h1>models of year constraction</h><p>{year}</p>')

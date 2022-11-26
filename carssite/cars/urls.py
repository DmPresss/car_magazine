from django.urls import path

from . views import *

app_name = 'cars'

urlpatterns = [
    path('', CarIndex.as_view(), name='index'),
    path('about/', about, name='about'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('loginout/', LoginoutUser, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CarCategory.as_view(), name='category'),
]

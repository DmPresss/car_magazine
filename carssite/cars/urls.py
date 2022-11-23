from django.urls import path

from . views import *

app_name = 'cars'

urlpatterns = [
    path('', CarIndex.as_view(), name='index'),
    path('about/', about, name='about'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CarCategory.as_view(), name='category'),


    # path('carsmodels/<slug:mod>/', cars_models),
    # path('yearofbuild/<int:year>/', year_of_build)

]

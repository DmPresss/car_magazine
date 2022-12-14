from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupVeiwSet

r1_router = DefaultRouter()
r1_router.register('cars', PostViewSet, basename='car')
r1_router.register('cats', GroupVeiwSet, basename='category')


urlpatterns = [
    path('r1/api-token-auth/', views.obtain_auth_token),
    path('r1/', include(r1_router.urls)),
]

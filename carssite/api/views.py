from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions


from cars.models import Car, Category
from . serializers import CarSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class GroupVeiwSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

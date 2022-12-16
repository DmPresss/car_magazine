from rest_framework import viewsets
from . permissions import AuthorOrReadOnly


from cars.models import Car, Category
from . serializers import CarSerializer, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [AuthorOrReadOnly]
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupVeiwSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

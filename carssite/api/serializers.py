from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from cars.models import Car, Category


class CarSerializer(serializers.ModelSerializer):

    author = SlugRelatedField(slug_field='username', read_only=True)
    cat = SlugRelatedField(
        slug_field='slug',  queryset=Category.objects.all())

    class Meta:
        model = Car
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

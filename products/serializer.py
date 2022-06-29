from rest_framework import serializers
from products.models import Category, Orders, Rate, product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class OrsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'


class UpdateRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = ('rate', 'comment')

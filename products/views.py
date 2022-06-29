from datetime import date
from telnetlib import STATUS
from unicodedata import category
from venv import create
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView
from ecommerce.custompagenation import CustomPagenation
from products import serializer
from products.models import Category, Orders, Rate, product
from django.db.models import Count
from rest_framework.authentication import TokenAuthentication
from products.permissions import IstheUser
from products.serializer import CategorySerializer, OrsersSerializer, ProductSerializer, RateSerializer, UpdateRateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.


class GetPruducts(ListAPIView):
    serializer_class = ProductSerializer
    model = product
    pagination_class = CustomPagenation

    def get_queryset(self):
        categoryId = self.kwargs['category']
        queryset = self.model.objects.filter(category=categoryId)
        return queryset


class GetTopRatedPruducts(ListAPIView):
    serializer_class = ProductSerializer
    model = product
    pagination_class = CustomPagenation

    def get_queryset(self):
        queryset = self.model.objects.filter(rate__gt=3)
        return queryset


class GetCategories(ListAPIView):
    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()


class MostSaledPruducts(ListAPIView):
    serializer_class = ProductSerializer
    model = product

    def get_queryset(self):
        # queryset = self.model.objects.annotate(
        #     count=Count('id')).values('products',Count('id')).order_by('count').product
        # queryset = product.objects.filter(id__in=queryset)
        # select *from  products_orders_products ,products_orders where id=product_id  group by product_id order by count(product_id) desc limit 10
        queryset = product.objects.raw(
            'select * from products_product  where id in (select product_id  from products_orders_products  group by product_id order by count(product_id) desc limit 10)')
        return queryset


class NewRate(CreateAPIView):
    serializer_class = RateSerializer
    model = Rate
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UpdateRate(UpdateAPIView):
    model = Rate
    # queryset = Rate.objects.all()
    permission_classes = [IstheUser, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = UpdateRateSerializer

    def get_object(self):
        queryset = Rate.objects.get(pk=self.kwargs['pk'])
        return queryset

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.object.rate = serializer.data.get('rate')
            self.object.comment = serializer.data.get('comment')
            self.object.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors)

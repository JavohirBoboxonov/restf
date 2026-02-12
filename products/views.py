from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
# Create your views here.
@api_view(['GET'], )
def get_info(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    data = {
        'success':True,
        'products': serializer.data
    }
    return Response(data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()       
        data = {
            'success': True
        }
        return Response(data)
@api_view(['GET'])
def detail_product(request, pk):
    product = Product.objects.filter(pk = pk).first()
    if product is None:
        return 'Ma`lumot yo`q'
    serializer = ProductSerializer(product)

    detail = {
        "success": True,
        "message": "Product",
        "data": serializer.data
    }
    return Response(detail)

@api_view(['POST'])
def update_product(request,pk):
    product = Product.objects.filter(pk = pk).first()
    if product is None:
        return 'Malumot yo`q'
    serializer = ProductSerializer(product, data = request.data)
    if serializer.is_valid():
        serializer.save()

        data = {
            "success": True,
            "message": "Maxsulot yangilandi",
            "data": serializer.data
        }
        return Response(data)

@api_view(['GET'])
def delete_product(request, pk):
    product = Product.objects.filter(pk = pk).first()
    if product is None:
        return Response({
            "success": False,
            "message": "Maxsulot Topilmadi"
        }, status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product)
    deleted_data = serializer.data

    product.delete()

    data = {
        "success": True,
        "message": "Maxsulot o`chirildi",
        "data": deleted_data
    }
    return Response(data, status=status.HTTP_200_OK)
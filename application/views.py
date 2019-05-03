from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse

from .models import Details
from .serializers import DetailSerializers

@api_view(['GET', 'POST'])
def details_list(request, format=None):
    if request.method == 'GET':
        detail = Details.objects.all()
        serializer = DetailSerializers(detail, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_view(request, pk, format=None):
    try:
        detail = Details.objects.get(pk=pk)
    except Details.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DetailSerializers(detail)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DetailSerializers(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





'''
class DetailView(APIView):
    def get(self, request, pk=None):
        if pk:
            detail = get_object_or_404(Details.objects.all(), pk=pk)
            serializer = DetailSerializers(detail)
            return Response({"detail": serializer.data})
        details = Details.objects.all()
        serializer = DetailSerializers(details, many=True)
        return Response({"details": serializer.data})

    def post(self, request):
        detail = request.data.get('detail')
        serializer = DetailSerializers(data=detail)
        if serializer.is_valid(raise_exception=True):
            detail_saved = serializer.save()
        return Response({"success": "Details '{}' data is created successfully".format(detail_saved.Name)})

    def put(self, request, pk):
        detail_saved = get_object_or_404(Details.objects.all(), pk=pk)
        data = request.data.get('detail')
        serializer = DetailSerializers(instance=detail_saved, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            save_detail = serializer.save()
        return Response({"seccess": "Details '{}' data is updated seccessfully".format(save_detail.Name)})

    def delete(self, request, pk):
        detail = get_object_or_404(Details.objects.all(), pk=pk)
        detail.delete()
        return Response({"message": "Details with id '{}' your data has been deleted".format(pk)},status=204)
'''
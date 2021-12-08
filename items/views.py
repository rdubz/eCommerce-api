from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_items(request):

    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response({'items': serializer.data}, status=HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_item(request, item_id):

    item = Item.objects.get(id=item_id)
    serializer = ItemSerializer(item)

    return Response({'item': serializer.data}, status=HTTP_200_OK)


@api_view(['POST'])
def add_item(request):

    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=HTTP_200_OK)

    else:
        return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_item(request, item_id):

    item = Item.objects.get(pk=item_id)
    serializer = ItemSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=HTTP_200_OK)

    else:
        return Response(status=HTTP_400_BAD_REQUEST)
from .models import PromoCode
from .serializers import PromoCodeSerializer
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def create_promo_code(request):

    serializer = PromoCodeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=HTTP_200_OK)

    else:
        return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_promo_code(request, promo_code_id):

    promo_code = PromoCode.objects.get(pk=promo_code_id)
    serializer = PromoCodeSerializer(instance=promo_code, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=HTTP_200_OK)

    else:
        return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def delete_promo_code(request, promo_code_id):

    promo_code = PromoCode.objects.get(pk=promo_code_id)
    promo_code.delete()

    return Response(status=HTTP_200_OK)
from .models import PromoCode
from rest_framework import serializers


class PromoCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PromoCode
        fields = '__all__'

    def create(self, validated_data):
        promo_code = PromoCode.objects.create(**validated_data)

        return promo_code

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.percent_off = validated_data.get('percent_off', instance.percent_off)
        instance.max_usages = validated_data.get('max_usages', instance.max_usages)

        instance.save()
        return instance

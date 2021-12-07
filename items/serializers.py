from .models import Item, Size, Photo
from rest_framework import serializers


class SizeSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)

    class Meta:
        model = Size
        exclude = ['item', ]


class PhotoSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)

    class Meta:
        model = Photo
        exclude = ['item', ]


class ItemSerializer(serializers.ModelSerializer):
    sizes = SizeSerializer(many=True)
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'

    def create(self, validated_data):
        sizes_data = validated_data.pop('sizes')
        photos_data = validated_data.pop('photos')
        item = Item.objects.create(**validated_data)

        for size in sizes_data:
            Size.objects.create(item=item, **size)

        for photo in photos_data:
            Photo.objects.create(item=item, **photo)

        return item

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.sale_price = validated_data.get('sale_price', instance.sale_price)

        sizes = validated_data.get('sizes')

        for size in sizes:
            size_id = size.get('id', None)

            size_item = Size.objects.get(id=size_id, item=instance)
            size_item.size = size.get('size', size_item.size)
            size_item.quantity = size.get('quantity', size_item.quantity)
            size_item.save()

        instance.save()

        return instance

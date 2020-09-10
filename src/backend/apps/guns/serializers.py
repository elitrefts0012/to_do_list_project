from pprint import pprint

from rest_framework import serializers

from guns.models import Gun


class GunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gun
        fields = (
            'id',
            'manufacturer',
            'model',
            'caliber',
            'current_owner',
        )


class ForSaleGunSerializer(serializers.ModelSerializer):
    for_sale = serializers.BooleanField(required=True)

    class Meta:
        model = Gun
        fields = (
            'for_sale',
            'price',
            'stock_quantity',
            'id',
            'manufacturer',
            'model',
            'caliber',
            'current_owner',
        )

    def validate(self, attrs):
        if attrs['for_sale']:
            if 'price' not in attrs or 'stock_quantity' not in attrs:
                message = 'If for_sale is True, price(decimal) and stock_quantity(integer) fields are required.'
                raise serializers.ValidationError(message)
        if 'stock_quantity' in attrs and attrs['stock_quantity'] < 0:
            message = 'stock_quantity must be a non-negative integer.'
            raise serializers.ValidationError(message)
        return attrs

from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        """ metadata for Product """
        model = Product
        fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end')

    def to_representation(self, instance):
        # the method to serialize
        data = super().to_representation(instance)

        # add additional properties in serialized view
        data['is_on_sale'] = instance.is_on_sale()
        data['current_price'] = instance.current_price()

        return data

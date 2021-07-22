from django.test import TestCase
from store.models import Product


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
#
# import django
#
# django.setup()


def print_product(product):
    from store.serializers import ProductSerializer
    serializer = ProductSerializer()
    data = serializer.to_representation(product)
    import json
    from rest_framework.renderers import JSONRenderer
    renderer = JSONRenderer()
    print(renderer.render(data))
    print(json.dumps(data, indent=1))  # pretty print


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Mineral Water Strawberry',
                               description='Natural-flavored strawberry with an anti-oxidant kick.',
                               price=1.00,
                               photo='products/mineralwater-strawberry.jpg')

        import datetime

        x = datetime.datetime(2021, 7, 22)
        Product.objects.create(name='Mineral Water Strawberry',
                               description='Natural-flavored strawberry with an anti-oxidant kick.',
                               price=1.00,
                               sale_start=x,
                               sale_end=x,
                               photo='products/mineralwater-strawberry.jpg')

    def test_product_is_not_on_sale(self):
        """Animals that can speak are correctly identified"""
        product = Product.objects.all()[0]
        print_product(product)

        self.assertFalse(product.is_on_sale(), 'The product is not on sale')

    def test_product_is_on_sale(self):
        """Animals that can speak are correctly identified"""
        product = Product.objects.all()[1]
        print_product(product)

        self.assertTrue(product.is_on_sale(), 'The product is not on sale')

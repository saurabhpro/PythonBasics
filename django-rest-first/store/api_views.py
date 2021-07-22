from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

from store.models import Product
from store.serializers import ProductSerializer


class ProductsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class ProductList(ListAPIView):
    # get all products from db - we don't need to set this if we overwrite get_queryset
    queryset = Product.objects.all()

    # assign product serializer (the dto)
    serializer_class = ProductSerializer

    # define what kind of filtering we need and the id
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description')  # define tuples

    # define the support for limit offset pagination
    pagination_class = ProductsPagination

    # override the GenericView queryset method to support additional filtering - here we filter on 'on_sale'
    def get_queryset(self) -> queryset:
        # get from request params with default as None
        # http://127.0.0.1:8000/api/v1/products/?on_sale=false
        on_sale = self.request.query_params.get('on_sale', None)

        # uri without the flag
        if on_sale is None:
            return super().get_queryset()  # returns the predefined query set from line 17

        # queryset = Product.objects.all()
        if on_sale.lower() == 'true':
            from django.utils import timezone
            now = timezone.now()

            return self.queryset.filter(
                sale_start__lte=now,
                sale_end__gte=now,
            )

        return self.queryset


# post end point
class ProductCreate(CreateAPIView):
    """
         create a product instance.
    """
    serializer_class = ProductSerializer

    # *args Non-Keyword Arguments - just values
    # **kwargs Keyword Arguments - a dictionary with `key name : value`
    def create(self, request, *args, **kwargs):
        try:
            price = request.data.get('price')
            if price is not None and float(price) <= 0.0:
                raise ValidationError({'price': 'Must be above $0.00'})

        except ValueError:
            raise ValidationError({'price': 'A valid number is required'})

        return super().create(request, *args, **kwargs)


# combines RetrieveAPIView, UpdateAPIView, DestroyAPIView (get, put, patch, delete)
# note: there is a lot many combination so that we can use one URL
class ProductRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
       Retrieve, update or delete a product instance.
    """
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        """
            delete a product instance and clear django cache
        """
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete(f'product_data_{product_id}')
        return response

    def update(self, request, *args, **kwargs):
        """
            update a product instance and update django cache
        """
        # perform actual update using args on resource identified by request
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set(f'product_data_{product["id"]}', {
                'name': product['name'],
                'description': product['description'],
                'price': product['price'],
            })
        return response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
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

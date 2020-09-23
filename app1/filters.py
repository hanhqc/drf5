from django_filters import FilterSet

from app1.models import Computer


class ComputerFilter(FilterSet):
    from django_filters import filters
    # field_name中的列名需要与模型进行映射
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Computer
        fields = ['min_price', "max_price"]

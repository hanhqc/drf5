from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from app1.filters import ComputerFilter
from app1.models import Computer
from app1.pagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from app1.serializers import ComputerModelSerializer


class ComputerAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["brand", "price", "computer_name"]
    ordering = ["price"]


    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination

    # 查询价格大于3000  小于9000的电脑
    filter_class = ComputerFilter

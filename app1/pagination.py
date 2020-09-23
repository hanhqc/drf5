from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 5
    page_query_param = "page"


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = "limits"
    offset_query_param = "offsets"
    max_limit = 5


class MyCursorPagination(CursorPagination):
    cursor_query_param = "cursor"
    page_size = 3
    max_page_size = 5
    # ordering = "price"
    page_size_query_param = "page_size"


class LimitFilter:

    def filter_queryset(self, request, queryset, view):
        limit = request.query_params.get("limit")
        print(limit)
        if limit:
            limit = int(limit)
            return queryset[:limit]

        return queryset

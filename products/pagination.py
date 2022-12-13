
from rest_framework import pagination
from rest_framework.response import Response
from .serializers import ProductsSerializers
from rest_framework import status
class CustomPagination(pagination.PageNumberPagination):
    page_size = 1
    page_query_param= 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.page.next_page_number() if self.page.has_next() else None,
                'previous': self.page.previous_page_number() if self.page.has_previous() else None
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', 1)), 
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': ProductsSerializers(data, context={'request':self.request}, many=True).data
        }, status=status.HTTP_200_OK)

class CustomPaginationLimit(pagination.LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 50
    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return response
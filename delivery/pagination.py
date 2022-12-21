from .serializers import DeliPagination
from rest_framework import exceptions
from rest_framework.response import Response
def get_pagination_data(request, data):
    serializer = DeliPagination(data=request.data)

    if serializer.is_valid():
        return serializer.get(request, data)
    
    return serializer.errors
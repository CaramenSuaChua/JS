from drf_yasg import openapi

list_category = []
list_detail_category = []
create_category = openapi.Schema(
    title='asd',
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Caterory_name'),
    }) 
put_category = openapi.Schema(
    title='asd',
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Caterory_name'),
    }) 

del_category = []
 
list_products = []
list_detail_products = []
create_products = openapi.Schema(
    title='Products',
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Products_name'),
        'category': openapi.Schema(type=openapi.TYPE_STRING, description='Caterory_id'),
        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Products_quantity'),
        'price': openapi.Schema(type=openapi.TYPE_INTEGER, description='Products_price'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='Products_description'),
        'availibility': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Products_availibility'),
    }) 
put_products = openapi.Schema(
    title='Products',
    type=openapi.TYPE_OBJECT,
    properties={
        # 'id': openapi.Schema(type=openapi.TYPE_STRING, description='Products_id'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Products_name'),
        'category': openapi.Schema(type=openapi.TYPE_STRING, description='Caterory_id'),
        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Products_quantity'),
        'price': openapi.Schema(type=openapi.TYPE_INTEGER, description='Products_price'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='Products_description'),
        'availibility': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Products_availibility'),
    }) 

del_products = []
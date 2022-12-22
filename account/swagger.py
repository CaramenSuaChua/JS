from drf_yasg import openapi
# change_password_params = [
#     openapi.Parameter(
#         "old_password",
#         openapi.IN_QUERY,
#         format="password",
#         required=True,
#         type=openapi.TYPE_STRING,
#     ),
#     openapi.Parameter(
#         "new_password",
#         openapi.IN_QUERY,
#         format="password",
#         required=True,
#         type=openapi.TYPE_STRING,
#     ),
#     openapi.Parameter(
#         "retype_password",
#         openapi.IN_QUERY,
#         format="password",
#         required=True,
#         type=openapi.TYPE_STRING,
#     ),
# ]
change_password_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'old_password': openapi.Schema(type=openapi.TYPE_STRING, description='old_password'),
        'new_password': openapi.Schema(type=openapi.TYPE_STRING, description='new_password'),
        'retype_password': openapi.Schema(type=openapi.TYPE_STRING, description='retype_password',)
    }
)
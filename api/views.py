from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
def get_data(request):
    person = {'name': 'amin'}
    return Response(person)


@api_view(["POST"])
def auth(request):
    #TODO auth 
    ...

@api_view(["POST"])
def new_user(request):
    #TODO
    ...


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)
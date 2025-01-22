from django.http import JsonResponse
from base.rooms import rooms
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getRoutes(request):

    routes = [
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/update/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    return Response(rooms)


@api_view(['GET'])
def getRoom(request, pk):
    room = None
    for i in rooms:
        if i['_id'] == pk:
            room = i
            break
    return Response(room)

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from livre.models import Livre
from .serializer import LivreSerializer


@api_view(['GET'])
def getBooks(request):
    livres = Livre.objects.all()
    serializer = LivreSerializer(livres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getBook(request,id=None):
    livre = Livre.objects.get(id=id)
    serializer = LivreSerializer(livre)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addBook(request):
    serializer = LivreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateBook(request, id=None):
    livre = Livre.objects.get(id=id)

    serializer = LivreSerializer(instance=livre, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteBook(request, id=None):
    livre = Livre.objects.get(id=id)

    livre.delete()
    return Response("book deleted")

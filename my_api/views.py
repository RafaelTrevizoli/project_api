from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def listar_itens(request):
    itens = Item.objects.all()
    serializer = ItemSerializer(itens, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizar_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({"erro": "Item não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response({"erro": "Item não encontrado"}, status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response({"mensagem": "Item deletado com sucesso"}, status=status.HTTP_204_NO_CONTENT)


def home(request):
    return render(request, 'api/home.html')

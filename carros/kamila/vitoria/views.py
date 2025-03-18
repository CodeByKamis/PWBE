#os imports serve para que tais informações de outros documentos sejam reconhecidos nesse documento presente
from django.shortcuts import render
from .models import Carro
from .serializers import CarroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# ele serve para para listar todos os carros
@api_view(['GET'])
def read_carros(request):
    carros=Carro.objects.all()
    serializer = CarroSerializer(carros, many=True)#o many serve para pedir que mande a lista da forma que ela vem, crua, da forma que ela vem 
    return Response(serializer.data)#data é dados, n é data em portugues de data dd/mm/aaaa

# esse você usa para pesquisar um carro específico a partir da id dele
@api_view (['GET'])
def pegar_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializer(carro)
    return Response(serializer.data)


# esse serve para você postar um novo carro
@api_view(['POST'])
def create_carro(request):
    if request.method == 'POST':
        serializer = CarroSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# esse serve para editar as informações que você deseja sobre o carro a partir do id dele
@api_view(['PUT'])
def update_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarroSerializer(carro, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# esse serve para deletar o carro a partir da id dele
@api_view(['DELETE'])
def delete_carro(request, pk):
    try:
        carro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response({'erro': 'Carro inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    carro.delete()
    return Response({'Mensagem':f'O seu {carro.nome} foi apagado'}, status=status.HTTP_200_OK)

from django.shortcuts import render #combina um determinado modelo com um determinado dicionario de contexto e retorna um objetvo do tipo httpresponse
from .models import Postagem #importei a minha classe
from .serializers import EventoSerializer #importei a minha classe convertora
from rest_framework.response import Response #importei o response que serve para dar uma resposta
from rest_framework.decorators import api_view #importei uma tag que mostra quais metodos http eu vou usar
from rest_framework import status #importei o status que mostra os status das coisas
from datetime import datetime, timedelta #importei para conseguir filtrar os eventos de hoje até os prox 7 dias



@api_view(['GET'])#lista todos os eventos
def read_eventos(request):
    eventos = Postagem.objects.all()
   
    # FILTRAGEM POR CATEGORIA, É PASSADO A CATEGORIA E ELE VAI TE DAR O RETORNO
    categoria = request.query_params.get('categoria')
    if categoria:
        eventos = eventos.filter(categoria__icontains=categoria)

    # FILTRAGEM POR DATA, VOCÊ PASSA A DATA E ELE TE RETORNA OS EVENTOS COM SUA DATA E HORA
    date_time = request.query_params.get('date_time')
    if date_time:
        eventos = eventos.filter(data__icontains = date_time)

    # FILTRAGEM POR QUANTIDADE, VOCÊ PASSA A QUANTIDADE E ELE RETORNA A QUANTIDADE DE EVENTOS 
    quantidade = request.query_params.get('quantidade')
    if quantidade:
        eventos = eventos[:int(quantidade)]

    # ORDENAR OS EVENTOS POR DATA CRESCENTE E DECRESCENTE
    ordenando = request.query_params.get('ordenando')
    if ordenando == 'decrescente':
        eventos = eventos.order_by('-date_time')
    elif ordenando == 'crescente':
        eventos = eventos.order_by('date_time')

    # FILTRAR PARA OS PROXIMOS EVENTOS DOS PROXIMOS 7 DIAS
    dias = request.query_params.get('dias')
    hoje = datetime.now()
    sete_dias = hoje+timedelta(days=7)
    if dias == "7-dias":
        eventos = eventos.filter(date_time__gte=hoje, date_time__lte=sete_dias)

    # ELE RETORNA TODOS OS EVENTOS
    serializer = EventoSerializer(eventos, many=True)
    return Response (serializer.data)
    
    



@api_view (['GET'])#mostra apenas um específico pesquisando por id
def pegar_evento(request, pk):
    try:
        evento = Postagem.objects.get(pk=pk)
    except Postagem.DoesNotExist:
        return Response ({'erro': 'Evento inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializer(evento)
    return Response(serializer.data)



@api_view(['POST'])#cria um novo post
def create_evento(request):
    if request.method == 'POST':
        serializer = EventoSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])#serve para editar um post
def update_evento(request, pk):
    try:
        evento = Postagem.objects.get(pk=pk)
    except Postagem.DoesNotExist:
        return Response({'erro': 'Evento inexistente'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventoSerializer(evento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])#serve para deletar um post
def delete_evento(request, pk):
    try:
        evento = Postagem.objects.get(pk=pk)
    except Postagem.DoesNotExist:
        return Response({'erro': 'Evento inexistente'}, status=status.HTTP_404_NOT_FOUND)
    evento.delete()
    return Response({'Mensagem': f'O seu {evento.nome} foi apagado'}, status=status.HTTP_200_OK)
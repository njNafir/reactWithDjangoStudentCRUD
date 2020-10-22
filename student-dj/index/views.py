from django.http import Http404
from django.shortcuts import render
from ticket.models import Ticket

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Ticket
from .serializers import *

def index(request):
    try:
        t = Ticket.objects.all()
    except Ticket.DoesNotExist:
        raise Http404("Ticket does not exist")
    return render(request, 'index.html', {'ticket': t})


@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Ticket.objects.all()

        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def students_detail(request, pk):
    try:
        student = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
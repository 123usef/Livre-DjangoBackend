from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import bookserializer
from .models import *
# Create your views here.


@api_view()
def showbooks(request):
    books = Book.objects.all()
    seri = bookserializer(books , many=True)
    return Response(seri.data)


@api_view()
def showbook(request ,id):   
    book = Book.objects.get(id=id)
    seri = bookserializer(book , many=False)
    return Response(seri.data)
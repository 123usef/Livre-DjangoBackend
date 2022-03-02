from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import bookserializer , RegistrationSerialzer
from .models import *
# Create your views here.

#Registration view ready for API
@api_view(['POST'])
def RegistraionView(request):
    seri =RegistrationSerialzer(data=request.data)
    data={}
    if seri.is_valid():
        user_data = seri.save()
        data['response'] = "accounnt created succefully "
        data["username"] = user_data.username
        data["email"] = user_data.email
    else:
        data = seri.errors
    return Response(data)    




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
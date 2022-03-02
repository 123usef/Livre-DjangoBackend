from pickle import GET
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import *
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


#Main_User_Profile
@api_view()
def profile(request):
    user = request.user
    main_user_serializer = mainuserserializer(user, many=False)
    return Response(main_user_serializer.data)


@api_view(['POST'])
def manage_profile(request):
    user = request.user
    update_user = mainuserserializer(request.POST ,instance=user )
    if update_user.is_valid():
        update_user.save()
    return Response(update_user.data)


#User_Profile
@api_view(['GET'])
def others_profile(request, id):
    user = User.objects.get(id = id)
    other_user_serializer = otheruserserializer(user, many=False)
    return Response(other_user_serializer.data)
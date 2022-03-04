from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizer import RegistrationSerializer, Userserializer, bookserializer
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

# {
#  "username" : "nour2",
#  "email" : "nour@gmail.com",
#  "password":"nour12",
#  "password2" : "nour12",
#  "gender" : "male",
#  "date_of_birth" : "1999-07-12",
#  "location" : "cairo",
#  "phone" : "01272639811"
#  }
@api_view(['POST'])
def registration_view(request):
	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			user = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = user.email
			data['username'] = user.username
		else:
			data = serializer.errors
		return Response(data)
     

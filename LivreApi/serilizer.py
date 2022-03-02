from rest_framework import serializers
from .models import *



# Registration serializer getting cooked for view
class RegistrationSerialzer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','user_gender','date_of_birth','phone','location','password']
        extra_kwargs = {
                    'password1':{'write_only':True},
                    'password2':{'write_only':True}
        }



class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
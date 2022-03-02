# from dataclasses import field
# import email
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ['username' , 'email', 'gender' , 'date_of_birth','location','phone','password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self,validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user  
       

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


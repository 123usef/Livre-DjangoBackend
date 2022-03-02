from rest_framework import serializers
from .models import *

class mainuserserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class otheruserserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','gender','date_of_birth','location']

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
from rest_framework import serializers
from .models import *

class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):

	password2= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password', 'password2', 'gender' , 'date_of_birth' , 'location' , 'phone']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		user = User(
					email=self.validated_data['email'],
					username=self.validated_data['username'],
                    gender= self.validated_data['gender'],
                    date_of_birth = self.validated_data['date_of_birth'],
                    location = self.validated_data['location'],
                    phone = self.validated_data['phone'],
				  )
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		user.set_password(password)
		user.save()
		return user
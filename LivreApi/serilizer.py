from dataclasses import fields
from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

#main user
class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
#other user
class OtherUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','gender','date_of_birth','location']
#book 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

#register
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

#category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

#subscription        
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        
#unsubscription
class UnSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
#usersubcribtion        
class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields =' __all__'              

#messege              
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'   
#transactions
class TransactionSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'
#Rate
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'        
        
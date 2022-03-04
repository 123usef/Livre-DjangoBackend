from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
   
    is_blocked = models.BooleanField(default=False , null = True)
    is_admin = models.BooleanField(default=False , null = True)
    
    user_gender = (("male", "male"), ("female", "female"))
    gender = models.CharField(max_length= 6, choices=user_gender,null = True)
    date_of_birth = models.DateField(null = True)
    location = models.CharField(max_length = 200,null = True)
    phone = models.CharField(max_length = 20,null = True)
    email = models.EmailField(verbose_name = 'email',max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=50,null=True) 
    # book = models.ForeignKey(Book, on_delete= models.CASCADE)
    def __str__(self):
        return self.name

class Subscription(models.Model):
    cat = models.ForeignKey(Category, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return str(self.cat_id)
  
class Book(models.Model):
    title=models.CharField(max_length=50, null=True)
    author=models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    cat = models.ForeignKey(Category, on_delete= models.CASCADE)
    def __str__(self):
        return self.title

class Transaction(models.Model):
    type = models.CharField(max_length=50,null=True)
    tr_sender = models.ForeignKey(User,related_name ="tr_sender", on_delete= models.CASCADE)
    tr_receiver = models.ForeignKey(User,related_name="tr_receiver", on_delete= models.CASCADE)
    def __str__(self):
        return self.type

class Message(models.Model):
    content = models.CharField(max_length=250,null= True)
    m_sender = models.ForeignKey(User,related_name ="m_sender", on_delete= models.CASCADE)
    m_receiver = models.ForeignKey(User,related_name="m_receiver", on_delete= models.CASCADE)    
    def __str__(self):
        return self.content

class Rate(models.Model):
    rate = models.IntegerField(null=True)
    r_sender = models.ForeignKey(User,related_name ="r_sender", on_delete= models.CASCADE)
    r_receiver = models.ForeignKey(User,related_name="r_receiver", on_delete= models.CASCADE)      
    def __str__(self):
        return self.rate


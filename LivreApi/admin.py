from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Subscription)
admin.site.register(Transaction)
admin.site.register(Rate)

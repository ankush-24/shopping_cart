from django.contrib import admin
from rental.models import Friend,Belonging,Borrowed 
# Register your models here.
admin.site.register(Friend)
admin.site.register(Belonging)
admin.site.register(Borrowed)

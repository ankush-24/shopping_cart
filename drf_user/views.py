from django.contrib.auth.models import User
from rest_framework import viewsets
from drf_user import serializers

# Create your views here.


class UserViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer    

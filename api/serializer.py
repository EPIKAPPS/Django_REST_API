from rest_framework import serializers
from .models import Programmer
from django.contrib.auth.password_validation import validate_password

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'


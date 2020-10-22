from rest_framework import serializers
from .models import Ticket

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate')
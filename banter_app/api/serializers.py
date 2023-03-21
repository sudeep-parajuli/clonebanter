from rest_framework import serializers
from banter_app.models import *

class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateContact
        fields = "__all__"
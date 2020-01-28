from rest_framework import serializers
from .models import Add
class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model =Add
        fields = ('name', 'nid', 'fone')
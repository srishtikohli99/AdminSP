from rest_framework import serializers
from .models import File

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    link = serializers.CharField(max_length=2000)

# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = "__all__"
#         #fields = ('name', )

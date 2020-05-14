from rest_framework import serializers
# from .models import File

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    ids = serializers.CharField()
    name = serializers.CharField()
    age = serializers.CharField()
    gender = serializers.CharField()
    ids = serializers.CharField()
    fam_size = serializers.CharField()
    loc = serializers.CharField()



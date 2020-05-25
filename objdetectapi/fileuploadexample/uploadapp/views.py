from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from uploadapp import serializers
from .serializers import HelloSerializer
from .face_recognition import *
import requests


#from .models import objectDetect



class FileUploadView(APIView):
    # parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
        
        serializer =HelloSerializer(data=request.data)
        if serializer.is_valid():
            link = serializer.validated_data.get('link')

            print("here1")
            r = requests.get(link, allow_redirects=True)
            print("here2")
            open('hello.jpg', 'wb').write(r.content)
            print("here3")
        #serializer_class = serializers.HelloSerializer
        # serializer =HelloSerializer(data=request.data)
        # if serializer.is_valid():
        #     obj = serializer.validated_data.get('obj')
            
        #mod1 = objectDetect
            i = objectDetect()
            res = {"res":i}
            return Response(res, status=status.HTTP_201_CREATED)
        else:
            return Response("fail", status=status.HTTP_400_BAD_REQUEST)


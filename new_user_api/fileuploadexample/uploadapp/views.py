#from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from uploadapp import serializers
from .serializers import HelloSerializer
import requests
import time
import os
from .reco import *
import numpy as np
import os
import joblib
from sklearn.preprocessing import MinMaxScaler
dir_path = os.path.dirname(os.path.realpath(__file__))
dirs = os.path.join(dir_path,"X1.npy")
X = np.load(dirs,allow_pickle=True)
import pyrebase
import sklearn
import sklearn.metrics

config = {
    "apiKey": "AIzaSyD_jhgmfiRT2lo4gnpWMZy8UBgUGErsX8U",
    "authDomain": "customer-2e919.firebaseapp.com",
    "databaseURL": "https://customer-2e919.firebaseio.com",
    "projectId": "customer-2e919",
    "storageBucket": "customer-2e919.appspot.com",
    "messagingSenderId": "345832555767",
    "appId": "1:345832555767:web:88ec6218e7c3c263c2fff2",
    "measurementId": "G-0X3YPL8H78"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()




class FileUploadView(APIView):
    
    def post(self, request, *args, **kwargs):
        
        url_serializer = HelloSerializer(data=request.data)
        serializer_class = serializers.HelloSerializer
        serializer =HelloSerializer(data=request.data)
        if serializer.is_valid():
            ids = serializer.validated_data.get('ids')
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            gender = serializer.validated_data.get('gender')
            fam_size = serializer.validated_data.get('fam_size')
            loc = serializer.validated_data.get('loc')
            data = {"name":name, "age":age,"fam_size":fam_size,"loc":loc,"new":1,"gender":gender}
            print(ids)
            db.child(ids).set(data)
            print("here")
            # print(rec_items)
            return Response("hi", status=status.HTTP_201_CREATED)



# Recognise Faces using some classification algorithm - like Logistic, KNN, SVM etc.


# 1. load the training data (numpy arrays of all the persons)
		# x- values are stored in the numpy arrays
		# y-values we need to assign for each person
# 2. Read a video stream using opencv
# 3. extract faces out of it
# 4. use knn to find the prediction of face (int)
# 5. map the predicted id to name of the user 
# 6. Display the predictions on the screen - bounding box and name

import cv2
import numpy as np 
import os 
import time
#import keras
import tensorflow
#from tensorflow.keras.preprocessing import image
import tensorflow.keras as keras

print("hello")
from keras.models import load_model
#from keras import model
print("hello2")
from keras.models import model_from_json,Sequential
from keras.layers import Dense
print("hello3")
from keras.applications import ResNet50
import json
#with open("myfile.json", "r") as read_it: 
#     data = json.load(read_it) 
#print("hello4")

#json_file = open('myfile.json','r')
#loaded_model_json = json_file.read()
#json_file.close()
#model = model_from_json(loaded_model_json)
model = Sequential()

#1st layer as the lumpsum weights from resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
#NOTE that this layer will be set below as NOT TRAINABLE, i.e., use it as is
model.add(ResNet50(include_top = False, pooling = 'max', input_shape = (197,197,3)))

#model.add(AvgPooling2D(pool)) model.summary()
# model.add(Dense(2048 , activation = 'tanh'))
#model.add(Dense(1024 , activation = 'tanh'))
#model.add(Dense(1024 , activation = 'tanh')) 
#model.add(Dense(512 , activation = 'tanh'))
model.add(Dense(512, activation = 'tanh'))
model.add(Dense(256, activation = 'tanh'))
#model.add(Dense(256, activation= 'tanh'))
model.add(Dense(128, activation= 'tanh'))
model.add(Dense(64, activation= 'tanh'))
#model.add(Dense(32, activation= 'tanh'))
#2nd layer as Dense for 2-class classification, i.e., dog or cat using SoftMax activation
model.add(Dense(3, activation = "softmax"))
print("hello5")
#model=load_model('model.h5')
model.load_weights('model.h5')
print("hello6")

#img = cv2.imread("123.jpg")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#resized = cv2.resize(img, (197,197))
from tensorflow.keras.preprocessing.image import load_img,  img_to_array




########## KNN CODE ############
# def distance(v1, v2):
# 	# Eucledian 
# 	return np.sqrt(((v1-v2)**2).sum())

# def knn(train, test, k=5):
# 	dist = []
	
# 	for i in range(train.shape[0]):
# 		# Get the vector and label
# 		ix = train[i, :-1]
# 		iy = train[i, -1]
# 		# Compute the distance from test point
# 		d = distance(test, ix)
# 		dist.append([d, iy])
# 	# Sort based on distance and get top k
# 	dk = sorted(dist, key=lambda x: x[0])[:k]
# 	# Retrieve only the labels
# 	labels = np.array(dk)[:, -1]
	
# 	# Get frequencies of each label
# 	output = np.unique(labels, return_counts=True)
# 	# Find max frequency and corresponding label
# 	index = np.argmax(output[1])
# 	return output[0][index]
################################


#Init Camera

cap = cv2.VideoCapture("http://192.168.1.101:4747")

# Face Detection
# face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

# skip = 0
# # dataset_path = './data/'

# face_data = [] 
# labels = []

# class_id = 0 # Labels for the given file
# names = {} #Mapping btw id - name


# # Data Preparation
# for fx in os.listdir(dataset_path):
# 	if fx.endswith('.npy'):
# 		#Create a mapping btw class_id and name
# 		names[class_id] = fx[:-4]
# 		print("Loaded "+fx)
# 		data_item = np.load(dataset_path+fx)
# 		face_data.append(data_item)
# 		print(data_item.shape)

# 		#Create Labels for the class
# 		target = class_id*np.ones((data_item.shape[0],))
# 		class_id += 1
# 		labels.append(target)

# face_dataset = np.concatenate(face_data,axis=0)
# face_labels = np.concatenate(labels,axis=0).reshape((-1,1))

# print(face_dataset.shape)
# print(face_labels.shape)

# trainset = np.concatenate((face_dataset,face_labels),axis=1)
# print(trainset.shape)

# Testing 

while True:
	ret,frame = cap.read()
	if ret == False:
		continue

	# faces = face_cascade.detectMultiScale(frame,1.3,5)
	# if(len(faces)==3):
	# 	continue
	time.sleep(5)

	image = frame

	# for face in faces:
	# 	x,y,w,h = face

	# 	#Get the face ROI
	# 	offset = 10
	# 	face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
	# 	face_section = cv2.resize(face_section,(100,100))

	# 	#Predicted Label (out)
	# 	out = knn(trainset,face_section.flatten())

	# 	#Display on the screen the name and rectangle around it
	# 	pred_name = names[int(out)]
	# 	cv2.putText(frame,pred_name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
	# 	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

	cv2.imshow("Faces",frame)
	#resized = cv2.resize(image, (197,197))
	#cv2.imshow("Resized",image)
	cv2.imwrite("frame.jpg", frame) 
	break

	# key = cv2.waitKey(1) & 0xFF
	# if key==ord('q'):
	# 	break

img = load_img('frame.jpg', target_size=(197,197))
x = img_to_array(img)
x = x.reshape(1,197,197,3).astype('float')
#x /= 255

ans = model.predict(x)
print(ans)
# ans = model.predict("frame.jpg")
# print(ans)

cap.release()
cv2.destroyAllWindows()











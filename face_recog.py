# Team Members - Derrick Li and Jake Hosking
# Github Repository link: https://github.com/lishouyi1024/usc-ee250-fall2022-project-jake-derrick/tree/main

import face_recognition
import sys
import os
import pickle

# initial pickle setup
try:
    file = open("redekoppInc.pickle", "rb")
    redekoppInc = pickle.load(file)
except IOError:
    redekoppInc = 1

try:
    file = open("derrickInc.pickle", "rb")
    derrickInc = pickle.load(file)
except IOError:
    derrickInc = 1

try:
    file = open("jakeInc.pickle", "rb")
    jakeInc = pickle.load(file)
except IOError:
    jakeInc = 1

try:
    file = open("strangerInc.pickle", "rb")
    strangerInc = pickle.load(file)
except IOError:
    strangerInc = 1

# other initial setup

imagePath = sys.argv[1]
stranger = True

# passed in image
try:
    unknown_picture = face_recognition.load_image_file(imagePath)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
except IndexError:
    sys.exit("No face recognized in the picture")

# redekopp
picture_of_redekopp = face_recognition.load_image_file("redekopp.jpg")
redekopp_face_encoding = face_recognition.face_encodings(picture_of_redekopp)[0]

results = face_recognition.compare_faces([redekopp_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of Redekopp!")

    os.system("cp -u " + imagePath + " redekopp_images/redekopp" + str(redekoppInc) + ".jpg")
    stranger = False
    redekoppInc = redekoppInc + 1
    pickle.dump(redekoppInc, open("redekoppInc.pickle", "wb"))


# derrick 
picture_of_derrick = face_recognition.load_image_file("derrick.jpg")
derrick_face_encoding = face_recognition.face_encodings(picture_of_derrick)[0]

results = face_recognition.compare_faces([derrick_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of Derrick!")

    os.system("cp -u " + imagePath + " derrick_images/derrick" + str(derrickInc) + ".jpg")
    stranger = False
    derrickInc = derrickInc + 1
    pickle.dump(derrickInc, open("derrickInc.pickle", "wb"))

# jake
picture_of_jake = face_recognition.load_image_file("jake.jpg")
jake_face_encoding = face_recognition.face_encodings(picture_of_jake)[0]

results = face_recognition.compare_faces([jake_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of Jake!")
    
    os.system("cp -u " + imagePath + " jake_images/jake" + str(jakeInc) + ".jpg")
    stranger = False
    jakeInc = jakeInc + 1
    pickle.dump(jakeInc, open("jakeInc.pickle", "wb"))



if stranger == True:
    print("It's a picture of a stranger!")
    
    os.system("cp -u " + imagePath + " stranger_images/stranger" + str(strangerInc) + ".jpg")
    strangerInc = strangerInc + 1
    pickle.dump(strangerInc, open("strangerInc.pickle", "wb"))
Team Members - Derrick Li and Jake Hosking

Github Repository link: https://github.com/lishouyi1024/usc-ee250-fall2022-project-jake-derrick/tree/main

How to Execute:
        The project requires that you use the Raspberry Pi Camera Module v2 in order
    to take the photos, so this cannot be easily run on one's own Raspberry Pi
    without it. 

        The program consists of two edges, the Raspberry Pi running tcp_server.py 
    and a laptop or other linux device running tcp_client.py, face_detect.py, 
    face_recog.py, and handling the storage of the photos. You must ssh into 
    the RPi with copied ID (ssh-copy-id pi@"") in order for the scp file transfer\
    to operate correctly, and then run tcp_server.py. The laptop or linux device would 
    then run tcp_client.py, and follow the prompts to take the photos and 
    analysis them.

External Libraries:
    OpenCV/cv2 - A python library for computer vision that we used 
                 to find faces in the images, draw boxes around them
                 and compare them to our stock photos to catagorize who
                 is in the photo.
    
    Pickle - A python library for binary encoding of data that we used to
             number the images in their respective image directories (acts
             as a sudo global variable across all instances of face_recog.py).

    PiCamera - A python library that we used to take photos on our Pi 
               Camera Module v2.
    
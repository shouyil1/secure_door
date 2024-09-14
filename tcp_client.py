# Team Members - Derrick Li and Jake Hosking
# Github Repository link: https://github.com/lishouyi1024/usc-ee250-fall2022-project-jake-derrick/tree/main

from fileinput import close
import socket
import os

def main():
    
    # HOST = socket.gethostname()
    
    PORT = 8080
    
    HOST = "192.168.43.75" 
    
    # Create a socket and connect it to the server at the designated IP and port
    s = socket.socket()
    s.connect((HOST, PORT))
    
    # Get user input and send it to the server using TCP socket
    photosNum = input("How many photos (1-10): ").strip()
    while not photosNum.isdigit() or int(photosNum) > 10 or int(photosNum) < 1:
        print("Invalid input")
        photosNum = input("How many photos (1-10): ").strip()
    photosNum = int(photosNum)

    interval = input("Time interval between photos (0-10 seconds): ").strip()
    while not interval.isdigit() or int(interval) > 10 or int(interval) < 0:
        print("Invalid input")
        interval = input("Time interval between photos (0-10 seconds): ").strip()
    interval = int(interval)

    message = str(photosNum) + "," + str(interval)
    s.send(message.encode())
    
    # Receive a response from the server

    data = s.recv(1024)
    
    print("Done taking photos!")
    print()
    
    # copy the img over from the rpi
    for i in range (1, photosNum+1):
        os.system("scp pi@liderric:/home/pi/usc-ee250-fall2022-project-jake-derrick/buffer" + str(i) + ".jpg /home/lsy/project-jake-derrick")

    # prompt the user which picture they want to analyze (enter "quit" to quit)
    userInput = input("Enter the picture number you want to analyze (q to quit): ").strip().lower()
    while userInput != "q":
        if not userInput.isdigit() or int(userInput) > photosNum or int(userInput) < 1:
            print("Invalid input")
            userInput = input("Enter the picture number you want to analyze (q to quit): ").strip().lower()
            continue
        os.system("python3 face_recog.py buffer" + userInput + ".jpg")
        os.system("python3 face_detect.py buffer" + userInput + ".jpg haarcascade_frontalface_default.xml ")
        print()
        userInput = input("Enter the picture number you want to analyze (q to quit): ").strip().lower()
    
    # delete buffers
    s.send("delete".encode())
    for i in range (1, photosNum+1):
        os.system("rm buffer" + str(i) + ".jpg")
    
    # close the TCP connection
    s.close()
    
if __name__ == '__main__':
    main()

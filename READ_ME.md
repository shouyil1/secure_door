# Security Camera with Facial Recognition

## Overview

This project involves creating a wireless security camera system with facial recognition capabilities. The system can be accessed and controlled via a TCP connection to capture photographs, analyze them for the presence of individuals, draw bounding boxes around faces, and identify specific individuals from a predefined set of images.

## System Architecture

The project consists of two main components:
1. **Raspberry Pi with Camera Module v2**: Acts as the TCP server, capturing images as per commands received.
2. **External Linux Device (Client)**: Runs a TCP client application that sends commands to the Raspberry Pi, receives images via SCP file transfer, and processes them using OpenCV for facial recognition.

## Components and Implementation

- **Raspberry Pi Camera Module v2**: Used for capturing images.
- **TCP Communication**: Facilitates command communication between the Raspberry Pi and the external Linux device.
- **SCP File Transfer**: Allows the transfer of captured images from the Raspberry Pi to the client for processing.
- **OpenCV**: A robust Python library used for facial recognition and face parameterization.
- **Pickle**: A Python library for encoding file names across multiple script instances.

### Facial Recognition Process

OpenCV uses a system of face encoding to parameterize faces for comparison, taking measurements like the distance between eyes, skin/eye/hair color, and nose size. The project uses pre-encoded versions of faces and compares them against newly captured images to identify individuals.

## Process

- Capture images using a Raspberry Pi and control it via a TCP client.
- Transfer images to a Linux device for facial recognition using SCP.
- Identify faces using a pre-trained model with OpenCV, drawing bounding boxes around detected faces.

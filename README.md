# Raspberry-Pi-SPJ-VIT

Computer Vision project for **human detection and entry/exit counting** using a **Raspberry Pi**.
The system processes images, videos, and live camera feeds to detect people and count them when they cross a virtual line.

## Project Overview

This project is part of a Computer Vision course and industry project. The goal is to build a lightweight system that can run on a Raspberry Pi and automatically count the number of people entering and exiting an area.

## Tools & Technologies

* Python
* OpenCV
* NumPy
* Raspberry Pi
* Laptop / Pi Camera

## Learning Stages

### 1. Image Processing

Basic operations on images using OpenCV.

* Read and display images
* Convert to grayscale
* Resize / rotate images
* Edge detection
* Thresholding

### 2. Object Detection

Detect people in images using computer vision models.

* Bounding boxes for detected people
* Human detection using OpenCV / lightweight models

### 3. Video Processing

Process video frame-by-frame.

* Read video files
* Apply detection on each frame
* Display processed frames

### 4. Real-Time Camera Detection

Use webcam or Pi camera for live detection.

* Capture live frames
* Detect humans in real time

### 5. People Counting

Count people entering and exiting using a virtual line.

* Track detected people
* Detect line crossing direction
* Update entry and exit counters

## Basic Pipeline

Camera → Frame Capture → Human Detection → Tracking → Line Crossing Logic → Entry/Exit Counter

## Future Work

* Optimize performance for Raspberry Pi
* Improve detection accuracy
* Deploy with Raspberry Pi camera module

SPJ

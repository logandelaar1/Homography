# Calibration Project

This project is a multi-faceted application that uses computer vision libraries (cv2, numpy) for image processing and Flask for web application construction. It primarily handles the task of calibration, with two primary modules: an image streaming and interaction module and a homography calculation module. Authored by [Logan deLaar](https://github.com/Logandelaar1).

## Image Streaming and Interaction (`app.py`)

This module provides a simple web application that hosts a streaming image feed from a specified source (camera, static image). Users can interact with this feed in real time, plotting points and having their positions logged. 

Key components include:

- The `ImageStream` class, which handles the acquisition and manipulation of the image stream. This includes drawing a grid on the image, setting dot positions, and preparing frames for the web interface.
- A series of Flask routes that enable the logging of data points and the dynamic updating of the dot's position.
- A template rendering route that serves the frontend.

## Frontend (`index.html`)

The frontend of the application, written in HTML, CSS and JavaScript, provides an interface for users to interact with the image stream. They can manually enter coordinates to position a dot on the video feed, log the current dot position, and directly click on the video feed to move the dot. 

## Homography Calculation (`homography.py`, `homography_sys.py`)

These scripts calculate a homography matrix based on predefined real-world coordinates and corresponding pixel coordinates. `homography.py` is an interactive script which allows users to input pixel coordinates and receive the corresponding real-world coordinates. `homography_sys.py` is a system-based version of the script that reads from command-line arguments.

## Usage

1. Run `app.py` to start the server.
2. Open a web browser and navigate to `localhost:5000`.
3. Interact with the video feed directly or use the form to position the dot.
4. Log data as required.

The homography scripts can be run directly from the command line, inputting the pixel coordinates as arguments in `homography_sys.py` or interactively in `homography.py`.

## Future Work

- Add code to stream from a live camera source.
- Improve the calibration accuracy with additional tools.
- Add an interface for defining the correspondence points for homography calculation.

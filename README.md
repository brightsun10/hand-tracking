---

# Real-Time Hand Movement Tracking with MediaPipe

This project provides a high-performance, real-time hand tracking application that runs on a live webcam feed. It is built using Google's MediaPipe framework for its speed and accuracy, and it features an interactive web interface created with Gradio.

The application is designed to be lightweight, fast, and easily deployable to platforms like Hugging Face Spaces.

---

## Features

High-Fidelity Hand Tracking: Utilizes the pre-trained MediaPipe Hands model to detect 21 3D landmarks on each hand.

Real-Time Performance: Optimized for processing live video streams with very low latency, making it suitable for interactive applications.

Multi-Hand Detection: Capable of detecting and tracking up to two hands simultaneously.

Simple and Clean UI: A web interface powered by Gradio allows for easy interaction and demonstration.

Deployment-Ready: The project is structured to be deployed on Hugging Face Spaces with no code changes.

---

## Tech Stack
Hand Tracking Framework: Google MediaPipe

Video I/O: OpenCV

Web Interface: Gradio

---

## Project Structure
.
├── app.py              # The main Gradio application code

├── requirements.txt    # Python dependencies for the project

└── README.md           # This documentation file

---

## Local Setup and Execution

#### 1. Create a Project Folder

Create a directory for your project and place the app.py and requirements.txt files inside it.

#### 2. Set Up a Virtual Environment

It is highly recommended to use a virtual environment to keep project dependencies isolated.

Create the virtual environment

python -m venv venv

Activate the environment

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

#### 3. Install Dependencies

Install all the required Python packages from the requirements.txt file.

pip install -r requirements.txt

#### 4. Run the Application

You are now ready to start the hand tracking application. Run the following command in your terminal:

python app.py

This will launch a local web server. Open your web browser and navigate to the URL provided (typically http://127.0.0.1:7860). You should see the Gradio interface with your live webcam feed.

---

## How It Works

Video Input: Gradio captures frames from your webcam in real-time.

Image Processing: Each frame is passed to the track_hand_movements function.

MediaPipe Detection: The MediaPipe Hands model processes the frame to find the location and landmarks of any hands present.

Visualization: If hands are detected, OpenCV is used to draw the landmarks (dots) and connections (lines) onto the frame.

Video Output: The annotated frame is sent back to the Gradio interface and displayed to the user.

This entire loop runs continuously, creating a smooth, real-time hand tracking experience.

---

## Author

Made with ❤️ by Nithin P (brightsun10)

---

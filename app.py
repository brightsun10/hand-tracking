import gradio as gr
import cv2
import mediapipe as mp
import numpy as np

# --- INITIALIZE MEDIAPIPE ---

# Initialize MediaPipe Hands solution
mp_hands = mp.solutions.hands
# Initialize MediaPipe Drawing utilities for visualization
mp_drawing = mp.solutions.drawing_utils
# Initialize the Hands model
hands = mp_hands.Hands(
    static_image_mode=False,      # Process a video stream
    max_num_hands=2,              # Detect up to two hands
    min_detection_confidence=0.7, # Minimum confidence value for detection
    min_tracking_confidence=0.5   # Minimum confidence value for tracking
)

print("MediaPipe Hands model initialized successfully.")

# --- HAND TRACKING FUNCTION ---

def track_hand_movements(video_frame):
    """
    Processes a single video frame to detect and track hand movements.

    Args:
        video_frame (np.ndarray): The input video frame from the webcam.

    Returns:
        np.ndarray: The video frame with hand landmarks and connections drawn on it.
    """
    if video_frame is None:
        return None

    # Create a writable copy of the frame to draw on
    annotated_frame = video_frame.copy()

    # For performance, mark the image as not writeable to pass by reference.
    annotated_frame.flags.writeable = False
    # Convert the BGR image to RGB.
    rgb_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame and find hands
    results = hands.process(rgb_frame)

    # Re-enable writing to the frame
    annotated_frame.flags.writeable = True

    # Draw the hand annotations on the image.
    if results.multi_hand_landmarks:
        # Loop through all detected hands
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks (the dots on the joints)
            mp_drawing.draw_landmarks(
                image=annotated_frame,
                landmark_list=hand_landmarks,
                # Draw connections (the lines between joints)
                connections=mp_hands.HAND_CONNECTIONS,
                # Style for the landmarks
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=4),
                # Style for the connections
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
            )
            
            # Optional: You can access individual landmark coordinates like this:
            # for id, lm in enumerate(hand_landmarks.landmark):
            #     h, w, c = annotated_frame.shape
            #     cx, cy = int(lm.x * w), int(lm.y * h)
            #     # For example, draw a circle on the wrist landmark (id 0)
            #     if id == 0:
            #         cv2.circle(annotated_frame, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

    return annotated_frame

# --- GRADIO INTERFACE ---

# Define the Gradio interface
iface = gr.Interface(
    fn=track_hand_movements,
    inputs=gr.Image(sources=['webcam'], type="numpy", streaming=True),
    outputs="image",
    title="Real-Time Hand Movement Tracking",
    description="This application uses Google's MediaPipe to detect and track hand landmarks in real-time from your webcam feed. It can detect up to two hands simultaneously.",
    live=True
)

# Launch the application
if __name__ == "__main__":
    iface.launch(debug=True)

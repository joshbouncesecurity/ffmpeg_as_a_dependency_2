#source for this code: https://medium.com/@anshulsjr6/detecting-and-blurring-human-faces-in-live-video-39fb6362db2c

import cv2
import imageio

# Load the pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')# Open a connection to the camera (0 represents the default camera)
cap = cv2.VideoCapture(0)# Create a writer object for saving frames as a GIF
output_gif = "output_blurred_faces.gif"
writer = imageio.get_writer(output_gif, mode='I', fps=10)while True:
    # Read a frame from the camera feed
    ret, frame = cap.read()    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Define the region of interest (ROI) for the face
        roi = frame[y:y + h, x:x + w]        # Apply Gaussian blur to the ROI
        roi = cv2.GaussianBlur(roi, (0, 0), sigmaX=30)        # Place the blurred ROI back into the original frame
        frame[y:y + h, x:x + w] = roi    # Display the frame with blurred faces
    cv2.imshow("Real-Time Face Blur", frame)    # Save the frame to the GIF
    writer.append_data(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break# Release the camera, close the OpenCV window, and close the GIF writer
cap.release()
cv2.destroyAllWindows()
writer.close()

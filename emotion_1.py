# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:10:49 2025

@author: COMPUTER
"""

import os
import cv2
import numpy as np
from tkinter import Tk, Label, Button, PhotoImage, Frame, messagebox as ms
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Constants
EMOTION_DICT = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
DATASET_PATH = "dataset"
# Stop automatically after this many captured samples (set to None to disable)
MAX_SAMPLES = 5

def create_cnn_model():
    """Create and return the CNN model."""
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))
    model.load_weights('model.h5')  # Pre-trained weights
    return model

def capture_emotions(model, max_samples=MAX_SAMPLES):
    """Capture emotions using webcam and store frames in corresponding folders.

    Stops automatically when `max_samples` images have been saved (per run).
    Set `max_samples=None` to require manual 'q' press as before.
    """
    cv2.ocl.setUseOpenCL(False)
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    sample_num = 0

    # Create or clear the dataset folder
    reset_dataset_folders()

    stop = False

    while True:
        ret, img = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            emotion_label = EMOTION_DICT[maxindex]

            sample_num += 1
            emotion_path = os.path.join(DATASET_PATH, emotion_label)
            cv2.imwrite(os.path.join(emotion_path, f"{sample_num}.jpg"), gray[y:y+h, x:x+w])
            cv2.putText(img, emotion_label, (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Stop if we've reached the requested number of samples
            if max_samples is not None and sample_num >= max_samples:
                stop = True
                break

        cv2.imshow('Video', cv2.resize(img, (1600, 960), interpolation=cv2.INTER_CUBIC))
        # Exit if user pressed 'q' or we've reached max samples
        if cv2.waitKey(1) & 0xFF == ord('q') or stop:
            break

    cap.release()
    cv2.destroyAllWindows()

    # Inform the user if we stopped automatically
    if stop:
        try:
            ms.showinfo("Info", f"Captured {sample_num} samples. Stopping capture.")
        except Exception:
            # If Tkinter messagebox fails (no display), just print
            print(f"Captured {sample_num} samples. Stopping capture.")

def reset_dataset_folders():
    """Delete existing dataset folders and create new ones."""
    if os.path.exists(DATASET_PATH):
        for folder in os.listdir(DATASET_PATH):
            folder_path = os.path.join(DATASET_PATH, folder)
            if os.path.isdir(folder_path):
                for file in os.listdir(folder_path):
                    os.remove(os.path.join(folder_path, file))
    else:
        os.makedirs(DATASET_PATH)
        for emotion in EMOTION_DICT.values():
            os.makedirs(os.path.join(DATASET_PATH, emotion))

def count_emotion_files():
    """Count the number of files for each emotion."""
    emotion_counts = {}
    for emotion in EMOTION_DICT.values():
        emotion_path = os.path.join(DATASET_PATH, emotion)
        count = len([f for f in os.listdir(emotion_path) if os.path.isfile(os.path.join(emotion_path, f))])
        emotion_counts[emotion] = count
    return emotion_counts
# def google():
#     from subprocess import call
#     call(["python","google.py"])
def display_emotion_counts():
    """Display a new GUI window showing emotion counts with background image and full-screen geometry."""
    emotion_counts = count_emotion_files()
    movie_emotion = max(emotion_counts, key=emotion_counts.get)

    # Initialize root window
    root = Tk()
    root.title("Emotion Counts")
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")  # Fullscreen

    # Load background image
    background_image = PhotoImage(file="img1.png")  # Ensure background.png exists
    background_label = Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Content frame with transparent background
    content_frame = Frame(root, bg='black',highlightbackground='red',padx=10, pady=10,)
    content_frame.place(relx=0.5, rely=0.5, anchor='center')

    Label(content_frame, text="Emotion Counts", font=("Arial", 16), bg='black', fg='white').pack(pady=10)

    for emotion, count in emotion_counts.items():
        Label(content_frame, text=f"{emotion}: {count}", font=("Arial", 14), bg='black',fg='white').pack(pady=5)

    Button(content_frame, text=f"Play Movie for {movie_emotion}", font=("Arial", 12),bg="#2980b9",fg="black",
           command=lambda: play_movie(movie_emotion)).pack(pady=5)
    # Button(content_frame, text=f"google", font=("Arial", 12),
    #        command=google).pack(pady=5)
    Button(content_frame, text=f"close", font=("Arial", 12),bg="#2980b9",fg="black",
           command=root.destroy).pack(pady=5)

    root.mainloop()

def play_movie(movie_emotion):
    """Play a movie or song based on the emotion."""
    message = f"Person is {movie_emotion}. Playing a movie for them."
    ms.showinfo("Message", message)
    print(message)
    from subprocess import call
    call(["python", f"{movie_emotion.lower()}_post.py"])

# Main function
if __name__ == "__main__":
    cnn_model = create_cnn_model()
    capture_emotions(cnn_model)
    display_emotion_counts()

import cv2
import pytesseract
for i in range(5):
    cap = cv2.VideoCapture(i)
    if cap.read()[0]:
        print(f"Camera index {i} is working!")
        cap.release()

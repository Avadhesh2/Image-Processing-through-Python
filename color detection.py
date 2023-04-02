import cv2
import numpy as np
from tkinter import filedialog
import tkinter as tk

# Create a file dialog window to select an image
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Load the image
image = cv2.imread("C:\\Users\\Aayushi\\AppData\\Local\\Temp\\Temp1_strip_images.zip\\image1.jpg")

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range of colors to identify
lower_range = np.array([0, 0, 0])
upper_range = np.array([255, 255, 255])

# Create a mask to identify pixels within the specified color range
mask = cv2.inRange(hsv_image, lower_range, upper_range)

# Calculate the mean color of the pixels within the mask
mean_color = cv2.mean(image, mask=mask)

# Print the mean color in BGR format
print("Mean color:", mean_color[:3])
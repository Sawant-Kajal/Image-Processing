import cv2
import numpy as np

# Specify the path to your image
image_path = "Dog.jpeg"  

# Load the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load the image. Please check the path.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a threshold to create a binary image
    _, binary_image = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Initialize a count for objects
    object_count = 0

    # Loop through detected contours and count them
    for contour in contours:
        object_count += 1
    
    # Print the count of objects
    print(f"Number of objects in the image: {object_count}")
    
    # Draw the contours on the original image (optional)
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Display the image with the contours
cv2.imshow('Counted Objects', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

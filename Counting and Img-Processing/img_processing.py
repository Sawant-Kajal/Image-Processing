import cv2

# Specify the image path
image_path = "Dog.jpeg"  

# Read the image
image = cv2.imread(image_path)

# Resize the image
resized_image = cv2.resize(image, (300, 300))

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Edges', edges)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

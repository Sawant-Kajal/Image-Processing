import cv2
import os
import numpy as np

portraits_path = "Portraits"

for filename in os.listdir(portraits_path):
    if filename.endswith(('.jpg', '.png')):
        image_path = os.path.join(portraits_path, filename)
        image = cv2.imread(image_path)

        fixed_height = 300
        aspect_ratio = image.shape[1] / image.shape[0]
        resized_width = int(fixed_height * aspect_ratio)

        original_resized = cv2.resize(image, (resized_width, fixed_height))
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)

        # Resize the gray and edge images to match the original resized height
        gray_image_bgr = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
        gray_image_resized = cv2.resize(gray_image_bgr, (resized_width, fixed_height))
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        edges_resized = cv2.resize(edges_bgr, (resized_width, fixed_height))

        # Add labels
        cv2.putText(original_resized, 'Original', (10, fixed_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(gray_image_resized, 'Grayscale', (10, fixed_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(edges_resized, 'Edges', (10, fixed_height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Combine images horizontally
        combined_image = np.hstack((original_resized, gray_image_resized, edges_resized))

        cv2.imshow('Processed Images', combined_image)
        cv2.waitKey(0)

cv2.destroyAllWindows()

import cv2

# Read an image from file
image = cv2.imread('image.jpg')

# Display the image in a window
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resize the image
resized_image = cv2.resize(image, (1000, 1000))

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Save the processed image to file
cv2.imwrite('processed_image.jpg', processed_image)
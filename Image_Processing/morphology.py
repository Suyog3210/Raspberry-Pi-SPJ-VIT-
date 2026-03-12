import cv2
import numpy as np

# read image
img = cv2.imread("../images/test.jpg")

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold to binary
_, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

# create kernel
kernel = np.ones((5,5),np.uint8)

# erosion
erosion = cv2.erode(thresh, kernel, iterations=1)

# dilation
dilation = cv2.dilate(thresh, kernel, iterations=1)

# opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# closing
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# save results
cv2.imwrite("../output/erosion.jpg", erosion)
cv2.imwrite("../output/dilation.jpg", dilation)
cv2.imwrite("../output/opening.jpg", opening)
cv2.imwrite("../output/closing.jpg", closing)

print("Morphological operations completed")

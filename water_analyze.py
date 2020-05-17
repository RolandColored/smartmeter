import cv2

img = cv2.imread('water/2019-01-26-18-21-48.jpg', 0)

rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 175, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))
cropped = rotated[400:1200, 600:1400]
#thresholded = cv2.adaptiveThreshold(cropped, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#laplacian = cv2.Laplacian(cropped, cv2.CV_64F, scale=0.1, delta=0.5)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

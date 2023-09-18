import cv2
image = cv2.imread("variant-1.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("result", hsv_image)
cv2.waitKey(5000)


import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255))
cv2.putText(img, "Mercury", (113, 180), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (188, 267), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth", (286, 267), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars", (381, 257), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (471, 107), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturn", (770, 110), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Uranus", (962, 125), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptune", (1107, 135), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.imwrite("Solar_System_With_Names (Output).jpg", img)
cv2.imshow("Output", img)
cv2.waitKey(0)
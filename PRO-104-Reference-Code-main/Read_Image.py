import cv2

img = cv2.imread("butterfly.jpg")

cv2.imshow("Display Image",img)

grey_img = cv2.cvtColor(img,cv2.COLOR_RBG2GRAY)

cv2.imshow ("Grayscale",grey_img)

cv2.waitKey(0)
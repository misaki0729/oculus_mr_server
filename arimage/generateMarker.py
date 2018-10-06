import cv2
import cv2.aruco as aruco

for i in range(50):
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

    generator = aruco.drawMarker(dictionary, i, 100)
    cv2.imwrite("./" + str(i) + '.png', generator)

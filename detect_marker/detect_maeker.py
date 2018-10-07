import cv2
import cv2.aruco as aruco
import numpy as np

dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) 
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    rc, img = capture.read()
    height, width, depth    = img.shape
    # div_n = 2
    # img = cv2.resize(img, (width*div_n, height*div_n))
    # height, width, depth    = img.shape

    corners, ids, rejectedImgPoints = aruco.detectMarkers(img, dictionary) #マーカを検出

    aruco.drawDetectedMarkers(img, corners, ids, (0,255,0)) #検出したマーカに描画する
    cv2.imshow('drawDetectedMarker', img) #マーカが描画された画像を表示

    # print(corners)
    # print(ids)
    # print(rejectedImgPoints)

    # 配列を初期化
    sPoints = [ [0]*2 ] * 4

    count = 0
    for i, corner in enumerate( corners ):
        points = corner[0].astype(np.int32)
        cv2.polylines(img, [points], True, (0,255,0), 2)
        cv2.putText(img, str(ids[i][0]), tuple(points[0]), cv2.FONT_HERSHEY_PLAIN, 2,(0,0,255), 2)
        # 射影変換のために、1,0,2,3の順番に直す

        if ids[i][0] == 0:
            sPoints[2] = points[0]
        if ids[i][0] == 8:
            sPoints[3] = points[0]
        if ids[i][0] == 19:
            if count == 0:
                sPoints[2] = points[0]
                count += 1
            else:
                sPoints[0] = points[0]
        if ids[i][0] == 29:
            sPoints[1] = points[0]
    print(sPoints)

    cv2.imshow('drawDetectedMarkers', img)
    # # cv2.imwrite(filename+'drawDetectedMarkers.png', img)

    # 射影変換
    # 右上、左上、左下、右下
    rect = np.array([
        [1280,0],
        [0,0],
        [0,720],
        [1280,720],
    ])

    pts1 = np.float32(sPoints)
    pts2 = np.float32(rect)
    # print(pts1)
    # print(pts2)
    M = cv2.getPerspectiveTransform(pts1,pts2)
    img = cv2.warpPerspective(img,M,(width, height))
    cv2.imshow('getPerspectiveTransform', img)
    # cv2.imwrite(filename+'getPerspectiveTransform.png', img)

    cv2.waitKey(1)
capture.release()
cv2.destroyAllWindows()
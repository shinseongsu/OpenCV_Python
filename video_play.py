import cv2

video_file = './video/big_buck.avi'

cap = cv2.VideoCapture(video_file)      # 동영상 캡처 객체 생성
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25)
        else:
            break
else:
    print("can't open video")

cap.release()
cv2.destroyAllWindows()
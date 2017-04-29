import cv2
import threading
from datetime import datetime
from FaceThread import *

# カメラをキャプチャ開始
cap = cv2.VideoCapture('http://172.16.42.136:8090/stream/video.mjpeg')

while True:
	ret, frame = cap.read()
	#frameを表示
	cv2.imshow('camera capture', frame)
	if(threading.activeCount() == 1):
		th = FaceThread(frame)
		th.start()

	#10msecキー入力待ち
	k = cv2.waitKey(10)
	#Escキーを押されたら終了
	if k == 27:
		break

#キャプチャを終了
cap.release()
cv2.destroyAllWindows()

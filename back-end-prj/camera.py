import os
os.environ['LD_PRELOAD'] = '/usr/lib/arm-linux-gnueabihf/libatomic.so.1'
import cv2
cap=cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()                        #读取帧
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #灰度化展示
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):          #按‘q’退出
        break
#释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
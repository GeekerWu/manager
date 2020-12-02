import cv2 as cv
cap=cv.VideoCapture(0)
while(True):
    ret, frame = cap.read()                        #读取帧
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #灰度化展示
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):          #按‘q’退出
        break
#释放资源并关闭窗口
cap.release()
cv.destroyAllWindows()
import cv2, time

video = cv2.VideoCapture(0)

while(1):

    check, frame =  video.read()

    print(check)
    #print(frame)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
video.release()
cv2.destroyAllWindows()

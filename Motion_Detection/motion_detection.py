import cv2

cap = cv2.VideoCapture("../videos/video.mp4")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

frame_count = 0

while ret:

    # resize for faster processing (important for Raspberry Pi)
    frame1 = cv2.resize(frame1,(320,240))
    frame2 = cv2.resize(frame2,(320,240))

    # compute frame difference
    diff = cv2.absdiff(frame1, frame2)

    # convert to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # blur to remove noise
    blur = cv2.GaussianBlur(gray,(5,5),0)

    # threshold to create binary image
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

    # dilate to fill gaps
    dilated = cv2.dilate(thresh,None,iterations=3)

    # find contours
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        # ignore very small movements
        if cv2.contourArea(contour) < 500:
            continue

        x,y,w,h = cv2.boundingRect(contour)

        # draw bounding box
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)

    frame_count += 1

    frame1 = frame2
    ret, frame2 = cap.read()

cap.release()

# save final frame
if frame1 is not None:
    cv2.imwrite("../output/motion_result.jpg", frame1)

print("Motion detection completed")
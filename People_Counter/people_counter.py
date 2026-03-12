import cv2

# initialize HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# open video
cap = cv2.VideoCapture("../videos/video.mp4")

entry = 0
exit = 0

# virtual counting line
line_y = 120

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # resize frame for faster processing
    frame = cv2.resize(frame,(320,240))

    # detect people
    boxes, weights = hog.detectMultiScale(frame)

    for (x, y, w, h) in boxes:

        cx = int(x + w/2)
        cy = int(y + h/2)

        # draw bounding box
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        # draw centroid
        cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

        # check crossing
        if cy < line_y:
            entry += 1
        else:
            exit += 1

    # draw virtual line
    cv2.line(frame,(0,line_y),(320,line_y),(255,0,0),2)

    # save some frames
    if frame_count % 30 == 0:
        filename = "../output/count_" + str(frame_count) + ".jpg"
        cv2.imwrite(filename, frame)

    frame_count += 1

cap.release()

print("Entry count:", entry)
print("Exit count:", exit)
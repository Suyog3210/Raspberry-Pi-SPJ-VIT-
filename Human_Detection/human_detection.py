import cv2

# initialize HOG descriptor
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# open video
cap = cv2.VideoCapture("../videos/video.mp4")

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # resize for faster processing
    frame = cv2.resize(frame, (320,240))

    # detect people
    boxes, weights = hog.detectMultiScale(frame)

    for (x, y, w, h) in boxes:

        # draw bounding box
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    # save some frames
    if frame_count % 30 == 0:
        filename = "../output/human_detect_" + str(frame_count) + ".jpg"
        cv2.imwrite(filename, frame)

    frame_count += 1

cap.release()

print("Human detection completed")
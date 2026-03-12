import cv2

# open video
cap = cv2.VideoCapture("../videos/video.mp4")

# create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

frame_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # resize frame (faster for Raspberry Pi)
    frame = cv2.resize(frame, (320,240))

    # apply background subtraction
    fgmask = fgbg.apply(frame)

    # find contours of moving objects
    contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        if cv2.contourArea(contour) < 500:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        # draw bounding box
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    # save some frames
    if frame_count % 30 == 0:
        filename = "../output/bg_detect_" + str(frame_count) + ".jpg"
        cv2.imwrite(filename, frame)

    frame_count += 1

cap.release()

print("Background subtraction completed")
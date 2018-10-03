import cv2
import time

print('Accessing webcam...')
vs = cv2.VideoCapture(0)
time.sleep(1)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter('output_webcame.mp4', fourcc, 30.0, (int(vs.get(3)), int(vs.get(4))))

while True:
    frame = vs.read()
    frame = frame[1]

    cv2.imshow('Webcam', frame)
    video_writer.write(frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

vs.release()
video_writer.release()

print('Finished.')

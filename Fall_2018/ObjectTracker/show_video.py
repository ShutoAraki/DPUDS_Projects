import cv2

file_path = 'drone.mp4'
print(f'Reading from file {file_path}...')
vs = cv2.VideoCapture(file_path)

while True:
    frame = vs.read()
    frame = frame[1]

    if frame is None:
        break

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

vs.release()
print('Finished.')

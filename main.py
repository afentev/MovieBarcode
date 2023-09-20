import cv2
import numpy as np

vidcap = cv2.VideoCapture('/Users/user/Downloads/film.mkv')  # path to movie
success, image = vidcap.read()
total_frames = int(int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))  # * (1 - 81 / 1023))
length = 1024
c = total_frames // length

result = np.ndarray((image.shape[0], length, 3))

# for cap in range(c):
#     print(cap / c * 100)
#     frame_number = cap * c
#     vidcap.set(cv2.CAP_PROP_POS_FRAMES, frame_number - 1)
#     success, image = vidcap.read()
#     result[:, cap, :] = image.mean(axis=1)

count = -1
while success:
    count += 1
    print(count / total_frames * 100)
    success, image = vidcap.read()
    div, mod = divmod(count, c)
    if div >= length:
        break
    if mod != 0:
        continue
    result[:, div, :] = image.mean(axis=1)

cv2.imwrite("Barbie.png", result)     # save frame as .png file

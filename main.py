import cv2
import numpy as np
import concurrent.futures

# Path to the video file
video_path = '/Users/user/Downloads/film.mkv'
vidcap = cv2.VideoCapture(video_path)
total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

# Desired number of columns in the result image
length = 1024

# Calculate the step size
step = total_frames // length
frames = []

with concurrent.futures.ProcessPoolExecutor() as executor:
    success = True
    count = -1
    while success:
        count += 1
        print(count / total_frames * 100)
        success = vidcap.grab()
        div, mod = divmod(count, step)
        if div >= length:
            break
        if mod != 0:
            continue
        _, image = vidcap.retrieve()
        frames.append(executor.submit(lambda frame: frame.mean(axis=1), image))

vidcap.release()

height, width = frames[0].result().shape
result = np.empty((height, length, 3), dtype=np.uint8)

for i, mean_values in enumerate(frames):
    result[:, i, :] = mean_values.result()

cv2.imwrite("output.png", result)

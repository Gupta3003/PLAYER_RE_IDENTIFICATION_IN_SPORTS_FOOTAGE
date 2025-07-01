import cv2
import numpy as np

def extract_color_histogram(frame, box):
    x1, y1, x2, y2 = box
    player_img = frame[y1:y2, x1:x2]
    player_img = cv2.resize(player_img, (64, 128))
    hist = cv2.calcHist([player_img], [0, 1, 2], None, [8,8,8], [0,256]*3)
    return cv2.normalize(hist, hist).flatten()

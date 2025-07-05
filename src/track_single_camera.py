import cv2
import os
from src.detect import detect_players
from src.extract_features import extract_color_histogram
from src.utils import draw_box
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def track_players_single(video_path):
    cap = cv2.VideoCapture(video_path)
    output_path = f'static/outputs/annotated_single.mp4'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    writer = None
    player_features = {}
    id_counter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detect_players(frame)
        features = [extract_color_histogram(frame, box[:4]) for box in detections]
        assigned_ids = []

        for i, feat in enumerate(features):
            best_match = -1
            best_score = 0.5
            for pid, f in player_features.items():
                sim = cosine_similarity([feat], [f])[0][0]
                if sim > best_score:
                    best_match = pid
                    best_score = sim
            if best_match == -1:
                id_counter += 1
                best_match = id_counter
                player_features[best_match] = feat
            assigned_ids.append(best_match)
            draw_box(frame, detections[i][:4], best_match)

        if writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'avc1')
            writer = cv2.VideoWriter(output_path, fourcc, 30, (frame.shape[1], frame.shape[0]))
        writer.write(frame)

    cap.release()
    writer.release()
    return output_path

import cv2
import os
from src.detect import detect_players
from src.utils import draw_box
from src.extract_features import extract_color_histogram
from sklearn.metrics.pairwise import cosine_similarity

player_centers = {}

def annotate_and_save(video_path, player_features, id_counter, name_suffix):
    cap = cv2.VideoCapture(video_path)
    output_path = f'static/outputs/reid_cross/annotated_{name_suffix}.mp4'
    writer = None

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

            center = draw_box(frame, detections[i][:4], best_match)

            if best_match not in player_centers:
                player_centers[best_match] = {}
            player_centers[best_match][name_suffix] = center

        for pid, views in player_centers.items():
            if len(views) == 2:
                pts = list(views.values())
                cv2.line(frame, pts[0], pts[1], (255, 0, 0), 2)

        if writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'avc1')  # current line (likely using H264)
            writer = cv2.VideoWriter(output_path, fourcc, 30, (frame.shape[1], frame.shape[0]))
        writer.write(frame)

    cap.release()
    writer.release()
    return output_path, player_features, id_counter

def match_players_cross(path1, path2):
    global player_centers
    player_centers = {}

    player_features = {}
    id_counter = 0

    out1, player_features, id_counter = annotate_and_save(path1, player_features, id_counter, "view1")
    out2, _, _ = annotate_and_save(path2, player_features, id_counter, "view2")

    return {
        "view1": out1,
        "view2": out2
    }

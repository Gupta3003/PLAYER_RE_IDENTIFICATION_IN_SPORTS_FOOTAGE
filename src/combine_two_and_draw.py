import cv2
from src.detect import detect_players
from src.extract_features import extract_color_histogram
from sklearn.metrics.pairwise import cosine_similarity
from src.utils import draw_box

def combine_two_and_draw_lines(video1, video2, output_path='static/outputs/reid_cross/combined_two_lines.avi'):
    cap1 = cv2.VideoCapture(video1)
    cap2 = cv2.VideoCapture(video2)

    w1, h1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    w2, h2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

    width = w1 + w2
    height = max(h1, h2)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # or use 'MJPG'
    writer = cv2.VideoWriter(output_path, fourcc, 30, (width, height))

    player_features = {}
    id_counter = 0

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 or not ret2:
            break

        detections = []
        features = []
        centers = []

        for frame in [frame1, frame2]:
            det = detect_players(frame)
            feat = [extract_color_histogram(frame, box[:4]) for box in det]
            detections.append(det)
            features.append(feat)
            centers.append({})

        for cam_idx in range(2):
            for i, feat in enumerate(features[cam_idx]):
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

                centers[cam_idx][best_match] = draw_box(
                    [frame1, frame2][cam_idx], detections[cam_idx][i][:4], best_match
                )

        combined = cv2.hconcat([frame1, frame2])

        for pid in player_features.keys():
            if pid in centers[0] and pid in centers[1]:
                pt1 = centers[0][pid]
                pt2 = (centers[1][pid][0] + w1, centers[1][pid][1])
                cv2.line(combined, pt1, pt2, (255, 0, 0), 2)

        writer.write(combined)

    cap1.release()
    cap2.release()
    writer.release()
    return output_path

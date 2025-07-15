from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from src.track_single_camera import track_players_single
from src.match_cross_camera import match_players_cross
from src.combine_two_and_draw import combine_two_and_draw_lines

app = Flask(__name__)

# Uploads from user
UPLOAD_FOLDER = 'data/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Outputs (served from static)
SINGLE_OUTPUT_FOLDER = 'static/outputs/reid_single'
CROSS_OUTPUT_FOLDER = 'static/outputs/reid_cross'
app.config['SINGLE_OUTPUT_FOLDER'] = SINGLE_OUTPUT_FOLDER
app.config['CROSS_OUTPUT_FOLDER'] = CROSS_OUTPUT_FOLDER

# Create folders if missing
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SINGLE_OUTPUT_FOLDER, exist_ok=True)
os.makedirs(CROSS_OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/single_camera')
def single_camera():
    return render_template('single_camera.html')

@app.route('/cross_camera')
def cross_camera():
    return render_template('cross_camera.html')

@app.route('/upload_single', methods=['POST'])
def upload_single():
    file = request.files['singlevideo']
    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)

    # Run single-camera tracking
    track_players_single(input_path)

    # File paths for HTML
    input_video = f"uploads/{filename}"  # this resolves to data/uploads/filename but is shown from <video>
    output_video = "outputs/reid_single/annotated_single.mp4"

    return render_template('result_single.html',
                           input_video=input_video,
                           output_video=output_video)

@app.route('/upload_cross', methods=['POST'])
def upload_cross():
    # Uploaded videos
    broadcast = request.files['broadcast']
    tacticam = request.files['tacticam']

    broadcast_filename = secure_filename(broadcast.filename)
    tacticam_filename = secure_filename(tacticam.filename)

    path1 = os.path.join(app.config['UPLOAD_FOLDER'], broadcast_filename)
    path2 = os.path.join(app.config['UPLOAD_FOLDER'], tacticam_filename)

    broadcast.save(path1)
    tacticam.save(path2)

    # Run re-identification and match logic
    output_paths = match_players_cross(path1, path2)

    combined_video_path = combine_two_and_draw_lines(
        output_paths["view1"],
        output_paths["view2"],
        output_path=os.path.join(app.config['CROSS_OUTPUT_FOLDER'], "combined_video.mp4")
    )

    # Pass to template (HTML expects path from static/)
    input_videos = {
        'broadcast': f"uploads/{broadcast_filename}",
        'tacticam': f"uploads/{tacticam_filename}"
    }
    combined_video = os.path.relpath(combined_video_path, 'static')  # gives: outputs/reid_cross/combined_video.mp4

    return render_template('result_cross.html',
                           input_videos=input_videos,
                           combined_video=combined_video)

if __name__ == '__main__':
    app.run(debug=True)

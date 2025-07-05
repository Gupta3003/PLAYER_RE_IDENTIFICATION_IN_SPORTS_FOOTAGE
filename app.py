from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from src.track_single_camera import track_players_single
from src.match_cross_camera import match_players_cross
from src.combine_three_and_draw import combine_three_and_draw_lines

app = Flask(__name__)

# Folder paths
UPLOAD_FOLDER = 'static/uploads'
SINGLE_OUTPUT_FOLDER = 'static/outputs/reid_single'
CROSS_OUTPUT_FOLDER = 'static/outputs/reid_cross'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SINGLE_OUTPUT_FOLDER'] = SINGLE_OUTPUT_FOLDER
app.config['CROSS_OUTPUT_FOLDER'] = CROSS_OUTPUT_FOLDER

# Ensure necessary folders exist
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

    # Create output path
    output_filename = f"annotated_{filename}"
    output_path = os.path.join(app.config['SINGLE_OUTPUT_FOLDER'], output_filename)

    # Run processing
    track_players_single(input_path, output_path)

    input_video = f"uploads/{filename}"
    output_video = f"outputs/reid_single/{output_filename}"  # Relative to 'static/'

    return render_template('result_single.html',
                           input_video=input_video,
                           output_video=output_video)

@app.route('/upload_cross', methods=['POST'])
def upload_cross():
    broadcast = request.files['broadcast']
    tacticam = request.files['tacticam']
    overview = request.files['overview']

    # Secure filenames
    broadcast_filename = secure_filename(broadcast.filename)
    tacticam_filename = secure_filename(tacticam.filename)
    overview_filename = secure_filename(overview.filename)

    # Save uploaded videos
    path1 = os.path.join(app.config['UPLOAD_FOLDER'], broadcast_filename)
    path2 = os.path.join(app.config['UPLOAD_FOLDER'], tacticam_filename)
    path3 = os.path.join(app.config['UPLOAD_FOLDER'], overview_filename)

    broadcast.save(path1)
    tacticam.save(path2)
    overview.save(path3)

    # Step 1: Re-identification and save annotated videos to reid_cross
    output_paths = match_players_cross(path1, path2, path3, output_dir=app.config['CROSS_OUTPUT_FOLDER'])

    # Step 2: Combine three views and draw lines
    combined_video_path = combine_three_and_draw_lines(
        output_paths["broadcast"],
        output_paths["tacticam"],
        output_paths["overview"],
        output_dir=app.config['CROSS_OUTPUT_FOLDER']
    )

    input_videos = {
        'broadcast': f"uploads/{broadcast_filename}",
        'tacticam': f"uploads/{tacticam_filename}",
        'overview': f"uploads/{overview_filename}"
    }

    combined_video = os.path.relpath(combined_video_path, 'static')  # returns path like "outputs/reid_cross/combined.mp4"

    return render_template('result_cross.html',
                           input_videos=input_videos,
                           combined_video=combined_video)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import os
from src.track_single_camera import track_players_single
from src.match_cross_camera import match_players_cross
from src.combine_three_and_draw import combine_three_and_draw_lines  # NEW IMPORT

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/uploads'
app.config['OUTPUT_FOLDER'] = 'static/outputs'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/single_camera')
def single_camera():
    return render_template('single_camera.html')

@app.route('/upload_single', methods=['POST'])
def upload_single():
    file = request.files['singlevideo']
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(input_path)

    output_path = track_players_single(input_path)
    return render_template('result_single.html', video_path='static/outputs/annotated_single.mp4')

@app.route('/cross_camera')
def cross_camera():
    return render_template('cross_camera.html')

@app.route('/upload_cross', methods=['POST'])
def upload_cross():
    video1 = request.files['broadcast']
    video2 = request.files['tacticam']
    video3 = request.files['overview']

    path1 = os.path.join(app.config['UPLOAD_FOLDER'], video1.filename)
    path2 = os.path.join(app.config['UPLOAD_FOLDER'], video2.filename)
    path3 = os.path.join(app.config['UPLOAD_FOLDER'], video3.filename)

    video1.save(path1)
    video2.save(path2)
    video3.save(path3)

    # Step 1: Generate annotated videos and store player ID mappings
    output_paths = match_players_cross(path1, path2, path3)

    # Step 2: Create a combined video with lines
    combined_video_path = combine_three_and_draw_lines(
        output_paths["broadcast"],
        output_paths["tacticam"],
        output_paths["overview"]
    )

    return render_template(
        'result_cross.html',
        video_broadcast=os.path.relpath(output_paths["broadcast"], 'static'),
        video_tacticam=os.path.relpath(output_paths["tacticam"], 'static'),
        video_overview=os.path.relpath(output_paths["overview"], 'static'),
        video_combined=os.path.relpath(combined_video_path, 'static')  # NEW
    )

if __name__ == '__main__':
    app.run(debug=True)

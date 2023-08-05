import cv2
import numpy as np
from flask import Flask, render_template, Response, request
import threading

app = Flask(__name__)

# data log file
log_file = "log_data.txt"

class ImageStream:
    def __init__(self, image_source):
        self.image_source = image_source
        self.frame_lock = threading.Lock()
        self.frame = cv2.imread(self.image_source)
        self.dot_pos = None

    def draw_grid(self, frame, line_color=(220, 220, 220), thickness=1, type_=cv2.LINE_AA, x_scale=1024, y_scale=720):
        height, width, _ = frame.shape

        x_step = width / x_scale
        y_step = height / y_scale

        for x in range(x_scale + 1):
            x_px = int(x * x_step)
            cv2.line(frame, (x_px, 0), (x_px, height), color=line_color, lineType=type_, thickness=thickness)
            cv2.putText(frame, str(x), (x_px + 10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 0), thickness)

        for y in range(y_scale + 1):
            y_px = int(y * y_step)
            cv2.line(frame, (0, y_px), (width, y_px), color=line_color, lineType=type_, thickness=thickness)
            cv2.putText(frame, str(y), (20, y_px - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.85, (0, 0, 0), thickness)

    # ...rest of the class...

    def get_frame(self):
        frame = self.frame.copy()
        self.draw_grid(frame)
        if self.dot_pos is not None:
            x, y = self.dot_pos
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
            cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 0, 255), 1)
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def set_dot_position(self, x, y):
        self.dot_pos = (x, y)

# Routes, and rest of the app...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    def generate_frames():
        while True:
            frame = image_stream.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_dot_position', methods=['POST'])
def set_dot_position():
    x = int(request.form['x'])
    y = int(request.form['y'])
    image_stream.set_dot_position(x, y)
    return 'OK'

@app.route('/log_data', methods=['POST'])
def log_data():
    x_distance = request.form['xDistance']
    y_distance = request.form['yDistance']

    if image_stream.dot_pos is not None:
        x, y = image_stream.dot_pos
        with open(log_file, 'a') as file:
            file.write(f"({x},{y}) ; ({x_distance},{y_distance})\n")

    image_stream.set_dot_position(None)

    return 'OK'

@app.route('/click_event', methods=['POST'])
def click_event():
    x = int(request.form['x'])
    y = int(request.form['y'])
    image_stream.set_dot_position(x, y)
    return 'OK'

if __name__ == '__main__':
    # Image source
    image_source = "/Users/logandelaar/Desktop/Screenshot 2023-07-19 at 6.09.55 AM.jpg"

    image_stream = ImageStream(image_source)

    app.run(debug=True)

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    # Route to serve the HTML page
    return render_template('index.html')

@app.route('docs/assets/<path:filename>')
def assets(filename):
    # Route to serve the image file
    return send_from_directory('docs/assets/', filename)

if __name__ == '__main__':
    app.run(debug=True)

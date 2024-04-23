from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Assuming 'image.jpg' is inside the 'static' folder
    image_path = '.docs/assets/image.jpg'
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)

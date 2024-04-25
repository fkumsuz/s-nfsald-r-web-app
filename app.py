from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
 
image_folder = "images/image.jpg"
 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', image_path=image_folder )

if __name__ == '__main__':
    app.run(debug=True)

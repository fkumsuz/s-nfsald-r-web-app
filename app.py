from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html', image_files=resized_image_files)

if __name__ == '__main__':
    app.run(debug=True)
"""
BACKGROUND_COLOR ="white"# "#5F6F52"
TEXT_COLOR = "black"  #"#FEFAE0"

from flask import Flask, render_template
import os

app = Flask(__name__)

# Folder containing the images
image_folder = "static/images"
# Get the list of image files and names in the folder
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith((".jpg", ".jpeg", ".png"))]
print(image_files)
image_names = [os.path.splitext(os.path.basename(file))[0] for file in image_files]
print(image_names)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', image_files=image_files, image_names=image_names, background_color=BACKGROUND_COLOR, text_color=TEXT_COLOR)
=======
    # Assuming 'image.jpg' is inside the 'static' folder
    image_path = '/static/image.jpg'
    return render_template('index.html', image_path=image_path)
>>>>>>> 0b42268002c42abd933e5ffcb5dcfe4eca899d2d

if __name__ == '__main__':
    app.run(debug=True)

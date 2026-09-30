from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    base_path = os.path.join(app.static_folder, 'images')
    all_images = {}

    # Sir static/images madhe shodhel Sir
    if os.path.exists(base_path):
        for folder in os.listdir(base_path):
            folder_path = os.path.join(base_path, folder)
            if os.path.isdir(folder_path):
                files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))]
                all_images[folder] = files

    # Sir root var tumhi taklele avif photo pan wedding madhe dakhvel Sir
    root_images = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.avif'))]
    if root_images:
        if 'wedding' not in all_images:
            all_images['wedding'] = []
        all_images['wedding'].extend(root_images)

    return render_template('index.html', all_images=all_images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

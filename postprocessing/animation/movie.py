import os
import imageio
from pathlib import Path

png_dir = Path.cwd()
images = []


for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.v2.imread(file_path))
imageio.mimsave(Path.cwd()/'movie.mp4', images,fps=10)

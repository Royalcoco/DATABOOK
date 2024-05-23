nft_library/
│
├── assets/
│   ├── images/
│   └── videos/
│
├── nft_generator/
│   ├── __init__.py
│   ├── image_generator.py
│   ├── video_generator.py
│   ├── nft_creator.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
# Empty __init__.py
from PIL import Image, ImageDraw, ImageFont
import os

def generate_image(text, filename):
    width, height = 800, 600
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 40)
    textwidth, textheight = draw.textsize(text, font)

    x = (width - textwidth) / 2
    y = (height - textheight) / 2

    draw.text((x, y), text, font=font, fill='black')

    if not os.path.exists('assets/images'):
        os.makedirs('assets/images')

    image.save(f'assets/images/{filename}')
    return f'assets/images/{filename}'
from moviepy.editor import TextClip, CompositeVideoClip
import os

def generate_video(text, filename):
    clip = TextClip(text, fontsize=70, color='white', size=(800, 600))
    clip = clip.set_duration(10)  # 10 seconds
    clip = clip.set_position('center').on_color(color=(0, 0, 0))

    if not os.path.exists('assets/videos'):
        os.makedirs('assets/videos')

    video_path = f'assets/videos/{filename}'
    clip.write_videofile(video_path, fps=24)
    return video_path
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
import os

def create_nft(image_path, video_path, output_filename):
    image_clip = ImageClip(image_path).set_duration(10)
    video_clip = VideoFileClip(video_path).set_duration(10)

    final_clip = CompositeVideoClip([video_clip, image_clip.set_position("center")])

    if not os.path.exists('assets/nfts'):
        os.makedirs('assets/nfts')

    final_nft_path = f'assets/nfts/{output_filename}'
    final_clip.write_videofile(final_nft_path, fps=24)
    return final_nft_path
import shutil

def clean_assets():
    folders = ['assets/images', 'assets/videos', 'assets/nfts']
    for folder in folders:
        shutil.rmtree(folder, ignore_errors=True)
        os.makedirs(folder)
from nft_generator.image_generator.py import generate_image
from nft_generator.video_generator.py import generate_video
from nft_generator.nft_creator.py import create_nft
from nft_generator.utils.py import clean_assets

def main():
    clean_assets()

    image_path = generate_image('NFT Example', 'example_image.jpg')
    video_path = generate_video('NFT Video Example', 'example_video.mp4')
    
    nft_path = create_nft(image_path, video_path, 'final_nft.mp4')
    
    print(f'NFT created at {nft_path}')

if __name__ == '__main__':
    main()
Pillow==8.4.0
moviepy==1.0.3
# NFT Library

This project generates NFTs by combining JPEG images with video animations.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Running the Application

1. Run the main script to generate the NFTs:
    ```
    python main.py
    ```

## Directory Structure

- `assets/images` : Directory for generated images.
- `assets/videos` : Directory for generated videos.
- `assets/nfts` : Directory for final NFT files.

- `nft_generator` : Package for NFT generation.
    - `image_generator.py` : Module to generate images.
    - `video_generator.py` : Module to generate videos.
    - `nft_creator.py` : Module to create NFTs.
    - `utils.py` : Utility functions.
    
- `main.py` : Main script to generate NFTs.
- `requirements.txt` : List of required packages.
- `README.md` : Project documentation.
Now, you can run the main.py script to generate the NFTs:
    
python main.py
This will create an NFT by combining the generated image and video in the assets/nfts directory.

You can customize the text and filenames in the main.py script to create different NFTs. Feel free to modify the image and video generation functions to add more features and effects to your NFTs.

I hope this helps! Let me know if you have further questions!

Happy coding!
```

# NFT Library

This project generates NFTs by combining JPEG images with video animations.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
4. Run the main script to generate the NFTs:
    ```
    python main.py
    ```
5. Check the `assets/nfts` directory for the final NFT files.

## Directory Structure

- `assets/images` : Directory for generated images.
- `assets/videos` : Directory for generated videos.
- `assets/nfts` : Directory for final NFT files.

- `nft_generator` : Package for NFT generation.
    - `image_generator.py` : Module to generate images.
    - `video_generator.py` : Module to generate videos.
    - `nft_creator.py` : Module to create NFTs.
    - `utils.py` : Utility functions.
    
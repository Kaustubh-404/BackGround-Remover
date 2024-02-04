# Background Removal using OpenCV

This Python script utilizes the OpenCV library to remove the background from an image. It applies color segmentation in the HSV color space to isolate the background, then performs morphological operations to refine the mask, and finally applies the mask to the original image to remove the background.

## How to Use

1. Install the required dependencies listed in `requirements.txt`.
2. Run the `remove_background` function, providing the input image path and the desired output path as arguments.
3. The script will generate a new image with the background removed and save it to the specified output path.


### Requirements
Make sure you have the following libraries installed:

opencv-python: Library for computer vision tasks.
numpy: Library for numerical computations.
Install the dependencies using pip:

```
pip install -r requirements.txt
```
### Create Copy
If you want to create a copy of this repository, you can use the following commands:
```
# Clone the repository
git clone https://github.com/your-username/background-removal.git

# Navigate to the repository directory
cd background-removal

# run
python remove_background.py
```

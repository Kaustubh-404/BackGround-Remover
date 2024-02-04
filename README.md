# Background Removal using OpenCV
This Python script utilizes the OpenCV library to remove the background from an image. It applies color segmentation in the HSV color space to isolate the background, then performs morphological operations to refine the mask, and finally applies the mask to the original image to remove the background.

How to Use
Install the required dependencies listed in requirements.txt.
Run the remove_background function, providing the input image path and the desired output path as arguments.
The script will generate a new image with the background removed and save it to the specified output path.

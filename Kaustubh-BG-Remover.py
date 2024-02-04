import cv2
import numpy as np

def remove_background(image_path, output_path):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if image is None:
            raise FileNotFoundError("Image not found or cannot be read.")
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([0, 0, 120])
        upper_bound = np.array([179, 50, 255])
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        inverted_mask = cv2.bitwise_not(mask)
        result = cv2.bitwise_and(image, image, mask=inverted_mask)
        cv2.imwrite(output_path, result)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    input_image_path = r"./nameLogo.png"
    output_image_path = r"./outputfile.png"
    remove_background(input_image_path, output_image_path)

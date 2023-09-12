import cv2
import numpy as np

def expand_image(image, expansion_pixels):
    # Get the dimensions of the image
    height, width, channels = image.shape

    # Calculate new dimensions for the expanded image
    new_height = height + expansion_pixels
    new_width = width + expansion_pixels

    # Create a new white image
    expanded_image = np.ones((new_height, new_width, channels), dtype=np.uint8) * 255

    # Place the image in the middle of the expanded image
    y_offset = expansion_pixels // 2
    x_offset = expansion_pixels // 2
    expanded_image[y_offset:y_offset + height, x_offset:x_offset + width] = image

    return expanded_image

if __name__ == "__main__":
    # Load the image
    image = cv2.imread("overlay.png")

    if image is None:
        print("Image does not exist.")
    else:
        # Expand the image by 20 pixels in white
        expanded_image = expand_image(image, 20)

        # Save or display the expanded image
        cv2.imwrite("Expanded_compass.png", expanded_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

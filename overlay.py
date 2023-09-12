import cv2
import numpy as np
import random

def rotate_image(image, angle):
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Calculate the rotation matrix
    matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Rotate the image
    rotated_image = cv2.warpAffine(image, matrix, (width, height), borderValue=(255, 255, 255))

    return rotated_image

def overlay_images(background_img, overlay_img, x_pos, y_pos):
    # Get the dimensions of the background image
    bg_h, bg_w, _ = background_img.shape

    # Get the dimensions of the image to be overlaid
    overlay_h, overlay_w, _ = overlay_img.shape

    # Check if the second image fits within the specified position
    if x_pos < 0 or x_pos + overlay_w > bg_w or y_pos < 0 or y_pos + overlay_h > bg_h:
        print("Error: The second image does not fit within the background.")
        return None

    # Copy the background image
    combined_image = background_img.copy()

    # Place the second image at the specified position
    combined_image[y_pos:y_pos + overlay_h, x_pos:x_pos + overlay_w] = cv2.bitwise_and(overlay_img, combined_image[y_pos:y_pos + overlay_h, x_pos:x_pos + overlay_w])

    return combined_image

if __name__ == "__main__":
    # Load the background image
    background_image = cv2.imread("background.jpg")

    # Load the image to be overlaid
    overlay_image = cv2.imread("expanded_image.png")

    Bias = 250
    if background_image is None or overlay_image is None:
        print("Image files not found.")
    else:
        # Place the second image at a specific position
        bg_h, bg_w, _ = background_image.shape
        overlay_h, overlay_w, _ = overlay_image.shape
        print("overlay_H =", overlay_h)
        print("overlay_W =", overlay_w)

        amount_size = input('Enter amount:')
        type_obj = input('Enter type(1,2,non):')
        print("type =", type(type_obj))
        for i in range(int(amount_size)):
            if type_obj == "non":
                x_pos = random.randint(0, bg_w - overlay_w)
                y_pos = random.randint(0, bg_h - overlay_h)
                while (27 < x_pos < 338 or 340 < x_pos < 650) and (-36 < y_pos < 505):
                    x_pos = random.randint(0, bg_w - overlay_w)
                    y_pos = random.randint(0, bg_h - overlay_h)
                type_of = type_obj + "_no_"
            elif type_obj == "1":
                x_pos = random.randint(132, 340 - overlay_w)
                y_pos = random.randint(92, 505 - overlay_h)
                type_of = type_obj + "_yes_no_"
            elif type_obj == "2":
                x_pos = random.randint(443, 650 - overlay_w)
                y_pos = random.randint(92, 505 - overlay_h)
                type_of = type_obj + "_yes_no_"

            rotation_angle = random.randint(0, 360)
            rotate_overlay_image = rotate_image(overlay_image, rotation_angle)

            result_image = overlay_images(background_image.copy(), rotate_overlay_image, x_pos, y_pos)

            if result_image is not None:
                # Show the result
                cv2.imshow("Combined Image", result_image)
                name_of_image = "datas/" + type_obj + "/" + str(i) + ".jpg"
                cv2.imwrite(name_of_image, result_image)
                cv2.waitKey(1)

    cv2.destroyAllWindows()

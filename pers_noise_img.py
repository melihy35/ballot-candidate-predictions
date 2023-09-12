def add_salt_and_pepper_noise(image, noise_density):
    h, w= image.shape[:2]
    noise = np.random.rand(h, w)  # random coordinate
    image_copy = image.copy()

    # White dots (Salt)
    image_copy[noise < noise_density / 2] = 255

    # Black dots (Pepper)
    image_copy[noise > 1 - noise_density / 2] = 0

    return image_copy


import cv2
import numpy as np
amount_size = input('Enter amount:')
type_obj = input('Enter type(1,2,non):')
print("type = ",type(type_obj))


for i in range(int(amount_size)):
    # Determine corner points randomly
    path_of_image="datas/"+type_obj+"/"+str(i)+".jpg"
    synthetic_image = cv2.imread("Expanded_pusula.png")
    height, width = synthetic_image.shape[:2]
    top_left = [np.random.randint(0, width//5), np.random.randint(0, height//5)]
    top_right = [np.random.randint(5*width//7, width), np.random.randint(0, height//5)]
    bottom_left = [np.random.randint(0, width//5), np.random.randint(5*height//7, height)]
    bottom_right = [np.random.randint(5*width//7, width), np.random.randint(5*height//6, height)]


    # Original perspective
    src_points = np.array([top_left, top_right, bottom_left, bottom_right], dtype=np.float32)

    # Target perspective (e.g. a perspective viewed from the camera)
    dst_points = np.array([[0, 0], [width, 0], [0, height], [width, height]], dtype=np.float32)

    # Calculate the perspective transformation matrix
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    # Perspective image 
    perspective_image = cv2.warpPerspective(synthetic_image, M, (width, height))
    
    noise_density = 0.08  # Noise intensity (add 0.02 to 2% noise)
    

    # Salt-and-Pepper noise
    noisy_perspective_image = add_salt_and_pepper_noise(perspective_image, noise_density)

    # show results
    cv2.imshow("Perspektif ve Gürültü Etkisi", noisy_perspective_image)

    name_of_image="datas/"+type_obj+"/"+str(i)+"p.jpg"
    cv2.imwrite(name_of_image,noisy_perspective_image)
    cv2.waitKey(0)
print(noisy_perspective_image.shape)
cv2.destroyAllWindows()


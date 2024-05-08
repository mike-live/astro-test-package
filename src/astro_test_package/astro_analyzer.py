import cv2
def analyze_astro_image(image_path):
    I = cv2.imread(image_path)
    area = (I > 0).sum()
    return area
import cv2


def resize(image, width):
    r = float(width) / image.shape[1]
    dim = (width, int(image.shape[0] * r))
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)


def rotate(image):
    # grab the dimensions of the image and calculate the center
    # of the image
    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)

    # rotate the image by 180 degrees
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    return cv2.warpAffine(image, M, (w, h))


def crop(image, from_y, to_y, from_x, to_x):
    return image[from_x:to_x, from_y:to_y]

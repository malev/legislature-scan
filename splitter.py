import os
import sys
from datetime import date
import cv2
from skimage.filter import threshold_adaptive
import imutils
import transform


class Splitter(object):
    def __init__(self, image, created_at=date.today()):
        self.image = image
        self.created_at = created_at.strftime("%y-%m-%d")
        self.dir = ''

    def crop(self):
        self._make_dir()
        self._store_original()

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)

        (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

        # loop over the contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            # if our approximated contour has four points, then we
            # can assume that we have found our screen
            if len(approx) == 4:
                screenCnt = approx
                break

        warped = transform.four_point_transform(self.image, screenCnt.reshape(4, 2))

        # convert the warped image to grayscale, then threshold it
        # to give it that 'black and white' paper effect
        warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        warped = threshold_adaptive(warped, 250, offset = 10)
        warped = warped.astype("uint8") * 255

        height, width = warped.shape

        part_1 = imutils.crop(warped, 0, width*0.24, height * 0.267, height * 0.875)
        part_2 = imutils.crop(warped, width*0.24, width*0.46, height * 0.267, height * 0.875)
        part_3 = imutils.crop(warped, width*0.47, width*0.696, height * 0.267, height * 0.875)
        part_4 = imutils.crop(warped, width*0.696, width*0.968, height * 0.267, height * 0.875)

        cv2.imwrite(self._new_file('part_1.jpg'), part_1)
        cv2.imwrite(self._new_file('part_2.jpg'), part_2)
        cv2.imwrite(self._new_file('part_3.jpg'), part_3)
        cv2.imwrite(self._new_file('part_4.jpg'), part_4)

    def _make_dir(self, index=0):
      if os.path.exists(self._dir_name(index)):
        self._make_dir(index + 1)
      else:
        os.makedirs(self._dir_name(index))
        self.dir = self._dir_name(index)
      return self.dir

    def _dir_name(self, index):
      return "build/%s-%i" % (self.created_at, index)

    def _store_original(self):
        cv2.imwrite(self._new_file('original.jpg'), self.image)

    def _new_file(self, filename):
        return "%s/%s" % (self.dir, filename)


if __name__ == '__main__':
    print "Starting"

    image = cv2.imread(sys.argv[1])
    splitter = Splitter(image)
    splitter.crop()

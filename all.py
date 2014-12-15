import sys
import cv2
from pprint import pprint
from splitter import Splitter
from ocr import OCR
from counter import Counter


if __name__ == "__main__":
    print "Starting"
    image = cv2.imread(sys.argv[1])
    splitter = Splitter(image)
    cropped_dir = splitter.crop()
    columns = OCR('build/' + cropped_dir)()
    counter = Counter(columns)
    print counter.count()

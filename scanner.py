import sys
from session_scanner import *


if __name__ == "__main__":
    print "Starting"
    image = cv2.imread(sys.argv[1])
    splitter = Splitter(image)
    cropped_dir = splitter.crop()
    columns = OCR('build/' + cropped_dir)()
    counter = Counter(columns)
    print counter.count()

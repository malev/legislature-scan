import subprocess


class OCR(object):
    def __init__(self, image_dir):
        self.image_dir = image_dir

    def __call__(self):
        output = []
        for index in [1,2,3,4]:
            output.append(self._get_text(index))

        return output

    def _get_text(self, index):
        output = ''
        filename = '%s/part_%i.jpg' % (self.image_dir, index)
        subprocess.call(['tesseract', filename, 'output'])
        with open('output.txt', 'r') as f:
            output = f.read()
        return output


if __name__ == '__main__':
    ocr = OCR('build/14-09-23-0/')
    print ocr()

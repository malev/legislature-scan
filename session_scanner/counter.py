import os
import sys
import json
import cv2
from splitter import Splitter
from ocr import OCR
from representatives import representatives


class Counter(object):
    def __init__(self, columns):
        self.columns = columns
        self.cleaned = []
        self._clean()

        # self._validate()

    def _clean(self):
        for column in self.columns:
            reps = column.split('\n')
            temp = [self._clean_rep(rep) for rep in reps]

            self.cleaned.append([rep for rep in temp if self._valid_rep(rep)])
        return self.cleaned

    def count(self):
        output = {}
        lines = self.cleaned[0] + self.cleaned[1] + self.cleaned[2] + self.cleaned[3]

        for rep, line in zip(representatives, lines):
            output[rep] = self._curate_vote(line[-1])

        return output

    def store_votes(self, dirname):
        with open(os.path.join(dirname, 'votes.json', 'w')) as f:
            f.write(json.dumps(self.count()))

    def _curate_vote(self, vote):
        if vote == 'a':
            return "aye"
        elif vote == 'n':
            return 'nay'
        elif vote == 'p':
            return 'present'
        elif vote == 'e':
            return 'excused'
        elif vote == 'x':
            return 'excused fc'
        else:
            return '*'

    def _clean_rep(self, rep):
        return rep.strip().lower()

    def _valid_rep(self, rep):
        return rep != ''

    def _validate(self):
        if len(self.cleaned[0]) != 38:
            raise "Invalid column 0"
        if len(self.cleaned[1]) != 38:
            raise "Invalid column 1"
        if len(self.cleaned[2]) != 38:
            raise "Invalid column 2"
        if len(self.cleaned[3]) != 35:
            raise "Invalid column 3"


if __name__ == '__main__':
    print "Starting"

    # image = cv2.imread(sys.argv[1])
    # splitter = Splitter(image)
    # images_dir = splitter.crop()
    columns = OCR('buid/14-10-21-21')()

    counter = Counter(columns)
    print counter.count()

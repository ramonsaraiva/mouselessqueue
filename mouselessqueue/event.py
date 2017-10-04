import cv2
import os
import time


class Template(object):

    COLOR = cv2.IMREAD_COLOR
    GRAY = cv2.IMREAD_GRAYSCALE
    UNCHANGED = cv2.IMREAD_UNCHANGED

    def __init__(self, file, threshold):
        self.path = os.path.join('templates', file)
        self.data = cv2.imread(self.path, cv2.IMREAD_COLOR)
        self.threshold = threshold

    @property
    def size(self):
        return self.data.shape[::-1]


class Event(object):

    def __init__(self, template, callback, timeout=0, timeout_callback=None):
        self.template = template
        self.callback = callback
        self.timeout = time.time() + timeout if timeout else 0
        self.timeout_callback = timeout_callback
import os
import time

import cv2
import numpy as np

from PIL import ImageGrab


class Screen(object):

    WINDOW_NAME = 'data'

    def __init__(self):
        self.image = None
        self.data = None
        self.event = None

    @property
    def inverted_image_size(self):
        return (self.image.size[1], self.image.size[0])

    def normalize_data(self):
        self.data = cv2.cvtColor(self.data, cv2.COLOR_RGB2BGR)

    def get_data(self):
        self.image = ImageGrab.grab()

        self.data = np.array(
            self.image.getdata(), dtype='uint8'
        ).reshape(self.inverted_image_size + (3,))

        self.normalize_data()

    def get_match(self, template):
        return cv2.matchTemplate(
            self.data, template.data, cv2.TM_CCOEFF_NORMED)

    def initialize_window(self):
        cv2.namedWindow(self.WINDOW_NAME, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.WINDOW_NAME, 800, 600)

    def show_data(self, gray=False):
        cv2.imshow(self.WINDOW_NAME, self.data)
        cv2.waitKey(1)

    def draw_rectangle(self, point, size):
        cv2.rectangle(
            self.data, point,
            (point[0] + size[0], point[1] + size[1]),
            (0, 0, 255), 2)

    def capture(self):
        while True:
            self.get_data()
            location = self.check_template()
            if location:
                self.event.callback(location)
                break
            if (not location and self.event.timeout > 0
                    and time.time() >= self.event.timeout):
                self.event.timeout_callback()
                break

    def assign_event(self, event):
        self.event = event
        self.capture()

    def check_template(self):
        match = self.get_match(self.event.template)
        locations = np.where(match >= self.event.template.threshold)

        try:
            location = next(zip(*locations[::-1]))
        except StopIteration:
            return

        return location if location else None

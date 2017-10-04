import win32api as api
import win32con as con


class Point(object):

    def __init__(self, position):
        self.position = position

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]


class Mouse(object):

    def __init__(self):
        pass

    def move(self, position):
        self.point = Point(position)
        api.SetCursorPos(self.point.position)

    def click(self):
        api.mouse_event(
            con.MOUSEEVENTF_LEFTDOWN, self.point.x, self.point.y, 0, 0)
        api.mouse_event(
            con.MOUSEEVENTF_LEFTUP, self.point.x, self.point.y, 0, 0)

    def hold(self):
        api.mouse_event(
            con.MOUSEEVENTF_LEFTDOWN, self.point.x, self.point.y, 0, 0)

    def release(self):
        api.mouse_event(
            con.MOUSEEVENTF_LEFTUP, self.point.x, self.point.y, 0, 0)

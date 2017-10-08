import sys
pathList = sys.path
pathList.append('.')

import cv2
import numpy as np


from Inputs import inputFrame
from Inputs import settings

class TestSettings:

    def setup(self):
        print("setup      class:TestSettings, fixture test method")
        self.settings = settings.Settings()

    def teardown(self):
        print("teardown      class:TestSettings")

    def setup_class(cls):
        print("\nsetup class      class: %s, fixture test class" % cls.__name__)

    def teardown_class(cls):
        print("teardown class      class: %s" % cls.__name__)

    def test_constructorX(self):
        width = settings.g_width
        assert width == 640

    def test_constructorY(self):
        hight = settings.g_hight
        assert hight == 480

    def test_setFrSizeWidth(self):
        self.settings.setFrameSize(300,200)
        width = settings.g_width
        assert width == 300

    def test_setFrSizeHight(self):
        self.settings.setFrameSize(300,200)
        hight = settings.g_hight
        assert hight == 200

    def test_setAoIHightOK(self):
        self.settings.setAoISize(100, 200,100, 16)
        high = settings.g_AoIhight
        assert high == 16

    def test_setAoIWidthOk(self):
        self.settings.setAoISize(100, 200, 100, 16)
        width = settings.g_AoIWidth
        assert width == 100

    def test_setAoIWidthNOk(self):
        self.settings.setAoISize(100, 800, 100, 16)
        endX = settings.g_AoIEndX
        assert endX == 640

    def test_setAoIHightNOk(self):
        self.settings.setAoISize(100, 800, 100, 400)
        high = settings.g_AoIhight
        assert high == 1

class TestInputClass:

    def setup(self):
        print("setup      class:TestInput, fixture test method")
        self.inp = inputFrame.Input()

    def teardown(self):
        print("teardown      class:TestInput")

    def setup_class(cls):

        print("\nsetup class      class: %s, fixture test class" %cls.__name__)

    def teardown_class(cls):
        print("teardown class      class: %s" % cls.__name__)


class TestBinLine:

    def setup(self):
        print("setup      class:TestBinLine, fixture test method")
        self.settings = settings.Settings()
        # self.settings.setAoISize(100,500,100,16)
        self.inp = inputFrame.Input()
        #TODO use singleton for settings ?
        # self.inp.settings.setAoISize(100,500,100,16)
        self.img = cv2.imread("pics/device_grey.png", cv2.IMREAD_GRAYSCALE)
        self.frame = self.inp.readFrame(self.img)
        rows, cols = self.img.shape
        # rows, cols, channels = self.img.shape
        self.settings.setFrameSize(cols, rows)
        self.settings.setAoISize(100,500,100,16)

    def teardown(self):
        print("teardown      class:TestBinLine")

    def setup_class(cls):

        print("\nsetup class      class: %s, fixture test class" %cls.__name__)

    def teardown_class(cls):
        print("teardown class      class: %s" % cls.__name__)

    def testLineConst(self):
        self.inp.extractAoI()
        binLine = self.inp.binLine()
        length = binLine.size
        assert length == 400


import cv2
import numpy as np
import settings

class Input:

    def __init__(self):
        self.settings = settings.Settings()
        pass

    def setupVideo(self):
        self.cap = cv2.VideoCapture(self.cameraId)


    def readFrame(self, inputFrame):
        self.wholeFrame = inputFrame

    def getFrameFromCamera(self):
        # Capture frame-by-frame
        ret, frame = self.cap.read()
        if ret:
            self.wholeFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def extractAoI(self):
        self.aoiFrame = self.wholeFrame[settings.g_AoIStartX:settings.g_AoIEndX, settings.g_AoIStartY:settings.g_AoIEndY]

    def binLine(self):
        line = np.zeros((settings.g_AoIWidth, 1), np.uint32)
        lineNormalized = np.zeros((settings.g_AoIWidth, 1), np.uint32)
        for x in range(settings.g_AoIWidth):
            for y in range(settings.g_AoIhight):
                line[x] += self.aoiFrame[x, y]
            # normalize line
            lineNormalized[x] = line[x] // settings.g_AoIhight

        return lineNormalized

    def getBinLineFromeInputFrame(self):
        self.getFrameFromCamera()
        self.extractAoI()
        line = self.binLine()
        return line

# global vars are used as a trick
# to guarantee that all the users of Setting class
# have the actual and the same values

g_width = 640
g_hight = 480
g_AoIStartX = 0
g_AoIStartY = 240
g_AoIEndX = 640
g_AoIEndY = 241
g_AoIWidth = 0
g_AoIhight = 0


class Settings:
    def __init__(self):
        self.cameraId = 0

        global g_width
        global g_hight
        global g_AoIStartX
        global g_AoIStartY
        global g_AoIEndX
        global g_AoIEndY
        global g_AoIWidth
        global g_AoIhight

        g_width = 640
        g_hight = 480
        g_AoIStartX = 0
        g_AoIStartY = 240
        g_AoIEndX = 640
        g_AoIEndY = 241

        g_AoIWidth = g_AoIEndX - g_AoIStartX
        g_AoIhight = g_AoIEndY - g_AoIStartY

    def setFrameSize(self, width, hight):
        ''' by new setting on frame-size, AoI must be new defined'''
        global g_width
        global g_hight
        global g_AoIStartX
        global g_AoIStartY
        global g_AoIEndX
        global g_AoIEndY

        g_width = width
        g_hight = hight
        g_AoIEndX = g_width
        g_AoIStartX = 0
        g_AoIStartY = g_hight // 2
        g_AoIEndY = g_AoIStartY + 1

    def setAoISize(self, widthStart, widthEnd, hightStart, hightWidth):
        global g_width
        global g_hight
        global g_AoIStartX
        global g_AoIStartY
        global g_AoIEndX
        global g_AoIEndY
        global g_AoIWidth
        global g_AoIhight

        if widthEnd > g_width:
            g_AoIEndX = g_width
        else:
            g_AoIEndX = widthEnd

        if widthStart > g_width:
            g_AoIStartX = 0
        else:
            g_AoIStartX = widthStart

        if (hightWidth + hightStart) > g_hight:
            g_AoIEndY = g_hight
            g_AoIStartY = g_hight - 1
        else:
            g_AoIEndY = hightStart + hightWidth
            g_AoIStartY = hightStart
            if hightStart > g_hight:
                g_AoIStartY = g_hight // 2

        g_AoIWidth = g_AoIEndX - g_AoIStartX
        g_AoIhight = g_AoIEndY - g_AoIStartY


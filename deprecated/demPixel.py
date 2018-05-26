class demPixel:
    rawData = None
    x = None
    y = None
    measurements = []

    def __init__(self, demLine):
        self.rawData = demLine
        self.processLine(demLine)

    def processLine(self, rawData):
        for i, dataPoint in enumerate(rawData.split(" ")):
            if i == 0:
                self.x = self.scientificToFloat(dataPoint)
            elif i == 1:
                self.y = self.scientificToFloat(dataPoint)
            else:
                self.measurements.append(self.scientificToFloat(dataPoint))

    def scientificToFloat(self, scientificNumber):
        return float(scientificNumber);

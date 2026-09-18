import uuid


class TimeSeriesAnalysisResult:
    def __init__(self):
        self._id = uuid.uuid4() # Result Id

    @property
    def id(self):
        return self._id
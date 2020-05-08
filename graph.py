"""
A graph drawer
"""
from matplotlib import pyplot

from wav_analyzer import WavAnalyzer


class WavGraph:
    """
    Shows a graph of a parsed 'wav' file
    """

    def __init__(self, wav_obj: WavAnalyzer) -> None:
        """
        :param wav_obj: An analyzed wav file object
        """
        self.wav_obj = wav_obj
        pyplot.ylabel('Song level')

        points = []
        next_point = next(self.wav_obj.read_all())
        while next_point is not None:
            points.append(next_point)
            next_point = next(self.wav_obj.read_all())
        pyplot.plot([(self.wav_obj.chunk * i / self.wav_obj.frame_rate) for i in range(len(points))], points)
        pyplot.axis([0, (self.wav_obj.n_frames / self.wav_obj.frame_rate), 0, 150])

    def show(self):
        """
        Show the graph of the analyzes wav file
        """
        if self.wav_obj.is_analyzed:
            pyplot.show()
        else:
            raise RuntimeError('Wav object not analyzed')

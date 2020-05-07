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

        pyplot.plot(list(self.wav_obj.get_frames(20)))
        pyplot.ylabel('Song level')
        pyplot.show()

    def show(self):
        """
        Show the graph of the analyzes wav file
        """
        if self.wav_obj.is_analyzed:
            pyplot.show()
        else:
            raise RuntimeError('Wav object not analyzed')

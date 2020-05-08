"""
Wav file analyzer
"""
import wave
from typing import List, Iterator

from numpy import average


class WavAnalyzer:
    """
    Class that analyzes a wav file according to different fields
    """

    WAV_READ = 'rb'
    WAV_WRITE = 'wb'
    BPS_TO_KBITPS = 125
    MAX_POINTS = 128

    def __init__(self, file_path: str) -> None:
        """
        :param file_path: Path to the wav file to be analyzed
        """
        self.file_path: str = file_path
        self.wav_obj: wave.Wave_read = wave.open(self.file_path, self.WAV_READ)

        self.is_analyzed: bool = False
        """Whether the wav file has been analyzed yet or not"""
        self.n_channels: int = self.wav_obj.getnchannels()
        """Number of channels"""
        self.sample_width: int = self.wav_obj.getsampwidth()
        """Width of each sample in bytes"""
        self.frame_rate: int = self.wav_obj.getframerate()
        """Sampling frequency"""
        self.n_frames: int = self.wav_obj.getnframes()
        """Total number of frames"""

        self.chunk: int = int(self.n_frames / self.MAX_POINTS)
        """Chunk size to average samples"""

    def get_info(self) -> dict:
        """
        Retrieve information about the wav file (size, bitrate, sample width)

        :return: Information about the wav file
        """
        info = {
            'channels': self.n_channels,
            'sample_width': self.sample_width,
            'frame_rate': self.frame_rate,
            'frame_count': self.n_frames,
            'total_time': '%.2fs' % (self.n_frames / self.frame_rate),
            'sample_rate': '%.2fkbit/s' % (self.n_channels * self.frame_rate * self.sample_width / self.BPS_TO_KBITPS)
        }
        if self.is_analyzed:
            info.update({})
        else:
            info.update({'NOTE': 'Analyze the wav object to retrieve mor info'})

        return info

    def analyze(self) -> None:
        """
        Analyze the wav file
        """
        self.wav_obj.rewind()
        # self._skip_intro()
        # TODO: fill

        self.is_analyzed = True

    def _skip_intro(self) -> None:
        """
        Skip the empty intro of the wav
        """
        data = self.wav_obj.readframes(self.chunk)
        while not sum(bytearray(data)):
            data = self.wav_obj.readframes(self.chunk)

    def get_frames(self, n: int) -> List[int]:
        """
        Get average of n frames divided by chunk size

        :param n: Number of average frames
        :return: `n` average frames from the wav file
        """
        frames = []
        for _ in range(n):
            data = self.wav_obj.readframes(self.chunk)
            if not len(data):
                break
            frames.append(average(bytearray(data)))
        return frames

    def read_all(self) -> Iterator[float]:
        """
        Generator that yields the average value of all frames in the wav file
        """
        data = self.wav_obj.readframes(self.chunk)
        if not len(data):
            yield None
        yield average(bytearray(data))

    def close(self) -> None:
        """
        Close the wav file
        """
        self.wav_obj.close()

    def __repr__(self) -> str:
        if self.is_analyzed:
            return f'<Analyzed wav object [{self.file_path}]>'
        return f'<Ready-to-analyze wav object [{self.file_path}]>'

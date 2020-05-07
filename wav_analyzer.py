"""
Wav file analyzer
"""


class WavAnalyzer:
    """
    Class that analyzes a wav file according to different fields
    """

    def __init__(self, file_path: str) -> None:
        """
        :param file_path: Path to the wav file to be analyzed
        """
        self.file_path: str = file_path
        self.is_analyzed: bool = False
        """Holds whether the wav file has been analyzed yet or not"""

    def analyze(self) -> None:
        """
        Analyze the wav file
        """
        # TODO: fill

        self.is_analyzed = True

    def __repr__(self):
        if self.is_analyzed:
            return f'<Analyzed wav object [{self.file_path}]>'
        return f'<Ready-to-analyze wav object [{self.file_path}]>'

"""
Tone analyser main
"""
import sys

from graph import WavGraph
from wav_analyzer import WavAnalyzer


def main():
    """
    Analyse a wac file
    """
    if len(sys.argv) < 2:
        raise UserWarning("Please pass in a wav file path")
    file_name = sys.argv[1]

    wav_obj = WavAnalyzer(file_name)
    print(wav_obj.get_info())
    wav_obj.analyze()

    graph = WavGraph(wav_obj)
    graph.show()

    wav_obj.close()


if __name__ == '__main__':
    main()

from moviepy.video.io.VideoFileClip import VideoFileClip
import tempfile

class AudioBytesPlayer:

    def __init__(self):
        pass

    @staticmethod
    def get_audio(video_path):
        video = VideoFileClip(video_path)
        audio = video.audio

        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmpfile:
            audio.write_audiofile(tmpfile.name, fps=44100, nbytes=2, buffersize=2000)
            tmpfile.seek(0)
            print(tmpfile.name)
            return tmpfile.name
import pyaudio
import wave


class SoundPlayer:
    def __init__(self, file_name: str = "hugokaku.wav", dir: str = "./sounds/") -> None:
        self.file_name = dir+file_name
        self.chunk = 1024

    def play(self):
        p = pyaudio.PyAudio()
        stream = p.open(
            format=p.get_format_from_width(self.wf.getsampwidth()),
            channels=self.wf.getnchannels(),
            rate=self.wf.getframerate(),
            output=True
        )
        data = self.wf.readframes(self.chunk)

        while data != b'':
            stream.write(data)
            data = self.wf.readframes(self.chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def buildWave(self):
        self.wf = wave.open(self.file_name, "rb")
        return self


if __name__ == "__main__":
    # test
    sp = SoundPlayer()
    sp.play()

import os
import math
from pytube import YouTube
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def youTubeToMp3(segment_length=10):
    # YouTube till mp4
    url = "https://www.youtube.com/watch?v=08QtyrXDaZI&ab_channel=nectar"
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()
    video_path = f"{youtube.title}.mp4"

    # mp4 till mp3
    audio_path = f"{youtube.title}.mp3"
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)
    clip.close()
    os.remove(video_path)

    # Mp3 till WAV
    wav_path = f"{youtube.title}.wav"
    audio = AudioSegment.from_mp3(audio_path)
    audio.export(wav_path, format='wav')
    output_file_prefix = "./postaudio/"

    # Splitta audio till segment
    segment_duration_ms = segment_length * 1000
    total_segments = math.ceil(len(audio) / segment_duration_ms)

    for i in range(total_segments):
        start_time = i * segment_duration_ms
        end_time = (i + 1) * segment_duration_ms
        segment = audio[start_time:end_time]

        output_file = f"{output_file_prefix}{i+1}.wav"
        segment.export(output_file, format="wav")

    os.remove(audio_path)

youTubeToMp3()
print('Färdigt :)')
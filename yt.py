import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

# YouTube video URL
url = "https://www.youtube.com/watch?v=08QtyrXDaZI&ab_channel=nectar"

# Download YouTube video using pytube
youtube = YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download()

# Convert video to MP3 using moviepy
video_path = f"{youtube.title}.mp4"
audio_path = f"{youtube.title}.mp3"

clip = VideoFileClip(video_path)
clip.audio.write_audiofile(audio_path)

# Delete the video file
os.remove(video_path)

print(f"Video downloaded and converted to MP3: {audio_path}")

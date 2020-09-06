# pip install pytube

# In some system, you also need to download one extra module
# pip install pytube3

import pytube

video_url= input("Enter Youtube URL for Download Video: ")

youtube= pytube.YouTube(video_url)

video= youtube.streams.first()

video.download()  # you can define specific path inside download()

input()
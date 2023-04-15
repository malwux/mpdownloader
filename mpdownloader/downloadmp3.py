import pytube # pip install pytube

url = "https://youtu.be/rbT6P-jwkO4" # video url
video = pytube.YouTube(url)

stream = video.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first() # It downloads in mp4 but you can replace the format to .mp3 without problems
stream.download(output_path="C:\\path") # your path download

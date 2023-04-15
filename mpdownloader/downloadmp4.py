import pytube # pip install pytube

url = "https://youtu.be/sjBnWtbtubc" # url video
video = pytube.YouTube(url)

# Download the best video and audio quality available
stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download(output_path="C:\\path") # your path download

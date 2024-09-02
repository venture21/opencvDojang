import pafy

url = 'https://youtu.be/gvXsmI3Gdq8'
video = pafy.new(url)

print(video.title)

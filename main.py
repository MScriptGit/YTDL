#Made by MScript 2025
from pytubefix import Search
from pytubefix import YouTube
from threading import Thread

print("To Search, enter '1'")
print("To download audio, enter '2'")
print("To download audio from a playlist, enter '3'")

choice = input("Enter number of choice")

if (choice == 1):
    YTSearch()
else if (choice == 2):
    YTDownload()
else:
    YTPLDownload()

def YTSearch():
    userInput = input("Enter Search terms: ")
  
    listTitle = []
    listDuration = []
    listURL = []

    results = Search(userInput)
        
    for video in results.videos:
        listTitle.append(f'{video.title}')
        listDuration.append(f'Duration: {video.length} sec')
        listURL.append(f'URL: {video.watch_url}')
        
    return listTitle, listDuration, listURL

def YTDL(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only()
    file_path = ys.download(output_path="temp/Download")
    on_download_complete(file_path)

def YTDownload():
    url = input("Enter URL to download: ")

    Thread(target=YTDL, args=(url,)).start()

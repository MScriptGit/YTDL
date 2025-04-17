#Made by MScript 2025
import streamlit as st
from pytubefix import Search
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress
from threading import Thread

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
    file_path = ys.download(output_path="Download")
    on_download_complete(file_path)

def YTDownload():
    url = input("Enter URL to download audio: ")

    Thread(target=YTDL, args=(url,)).start()

def YTPlaylistDL():
    url = input("Enter URL to download audio from a playlist: ")
    pl = Playlist(url)
    prefixCounter = 1
    PLprefix = ""
    for video in pl.videos:
        if prefixCounter < 10:
            PLprefix = "0" + str(prefixCounter) + ". "
        else:
            PLprefix = "" + str(prefixCounter) + ". "
        ys = video.streams.get_audio_only()
        file_path = ys.download(output_path="temp/Downloaded_Playlists", filename_prefix=PLprefix)
        prefixCounter +=1
    on_download_complete()

def on_progress(stream, chunk, bytes_remaining):
    filesize = stream.filesize
    current = ((filesize - bytes_remaining) / filesize)
    percent = ('{0:.1f}').format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

def on_download_complete():
    print("Download voltooid!")

st.write("Tadaaa!")

print("To Search, enter '1'")
print("To download audio, enter '2'")
print("To download audio from a playlist, enter '3'")

choice = input("Enter number of choice")

if (choice == 1):
    YTSearch()
elif (choice == 2):
    YTDownload()
else:
    YTPLDownload()

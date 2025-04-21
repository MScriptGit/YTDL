#Made by MScript 2025
import streamlit as st
from pytubefix import Search
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress
from threading import Thread

def YTSearch(userInput):
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

def YTDownload(url):
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

def btn_clicked():
    if (choice == "Search"):
        listTitle, listDuration, listURL = YTSearch(userInput)
        """i = 0
        for x in listTitle:
            label = f"{x}\n{listDuration[i]}"
            if st.button(label):
                st.success(YTDownload(listUrl[i]))
            i += 1"""
        st.session_state.search_results = (listTitle, listDuration, listURL)
    elif (choice == "Download Audio"):
        YTDownload()
    elif (choice == "Download Playlist"):
        YTPlaylistDL()
    else:
        return false
        #add code to display input error

choice = st.radio("Choose option", ["Search", "Download Audio", "Download Playlist"])

userInput = st.text_input(label="Enter keywords to search or URL to download")

st.button(label="Let's go!", on_click=btn_clicked)

# Display search results if they exist in session state
if 'search_results' in st.session_state:
    listTitle, listDuration, listURL = st.session_state.search_results
    for i, title in enumerate(listTitle):
        label = f"{title}\n{listDuration[i]}"
        if st.button(label):
            st.success(YTDownload(listURL[i]))

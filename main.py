#Made by MScript 2025
from pytubefix import Search

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


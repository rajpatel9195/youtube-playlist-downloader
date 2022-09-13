from pytube import Playlist
from pytube.cli import on_progress
url = input("url ")
filename = input("filename ")
pl = Playlist(url)
print("Totle no. of videos" +  "  " + str(pl.length))
x=1
for vid in pl.videos:
    try:
        print(x , " is dwonloading... "  ,  "File size: " , str(round( vid.streams.get_highest_resolution().filesize / (1024 * 1024), 3)) , " MB")    
        print(vid.title)
        vid.register_on_progress_callback(on_progress)
        
        vid.streams.get_highest_resolution().download(filename)
        print(" ")
        x+=1
    except:
        continue

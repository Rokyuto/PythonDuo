import pytube
import os
from moviepy.editor import VideoFileClip

save_path = ""
content = ""
#temp_link = "https://youtu.be/Qpf26PtBXgo"
#temp_video_type = "mp4"
#temp_content_name = "Forever 1"

# Function to Choose Save Location/Directory
def f_chooseSavePath(path_to_save):
    global save_path
    save_path = path_to_save
    return save_path


def f_DownloadContent(link):
    global content
    try:
        content = pytube.YouTube(link)
        content = content.streams.get_highest_resolution()
        content.download()
    except:
        print("Error with Connection to YouTube")
      
  
#f_chooseSavePath()
#f_DownloadContent()

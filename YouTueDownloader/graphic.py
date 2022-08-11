from tkinter import *
from tkinter import filedialog
import pytube
from downloadVideo import *
from tkinter import messagebox

# Window specification
root= Tk()
root.title("YouTue Video Downloader")
label_path=""
root.geometry('500x500')
select_dir=Label(root,text='Select Directory',font=('italic 15'))
select_dir.pack(pady=50)

def get_directoryData():
    filepath=filedialog.askdirectory(initialdir='C:\Downloads',title='DirectoryPath')
    label_path=Label(root,text=filepath,font=("italic 20"))
    label_path.pack(pady=50)
    f_chooseSavePath(filepath)

button=Button(root,text='Choose Directory',command=get_directoryData,width=20,height=4,bg='gray',fg='white')
button.pack()

videoLinkPath=Text(root,width=40 ,height=5,bg='white',fg="black",font=('30'))
videoLinkPath.pack(pady=2)
content_type = "mp3"

def downloadVideo():
    global label_path
    global videoLinkPath
    global content_type
    inputValue=videoLinkPath.get("1.0","end-1c") # Get TextBox Value
    try: # Try Validate the Entered from the User YouTube Link
        pytube.YouTube(inputValue)
        messagebox.showinfo("Info","YouTube video started to download")
        f_DownloadContent(inputValue, content_type)
        messagebox.showinfo("Successfully","YouTube video downloaded successfully")
    except: # If NOT Valid
        print("Error")
        messagebox.showerror("Failed","YouTube video download failed")
        # Error Msg

button=Button(root,text='Download',command=downloadVideo,width=20,height=4,bg='green',fg='white')
button.pack()
root.mainloop()

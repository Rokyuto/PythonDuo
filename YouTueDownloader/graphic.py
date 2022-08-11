from tkinter import *
from tkinter import filedialog

# Window specification
root= Tk()
label_path=""
root.geometry('500x500')
select_dir=Label(root,text='select dir',font=('italic 14'))
select_dir.pack(pady=50)

def get_directoryData():
    
    filepath=filedialog.askdirectory(initialdir='C:\Downloads',title='DirectoryPath')
    label_path=Label(root,text=filepath,font=("italic 13"))
    label_path.pack(pady=50)

button=Button(root,text='getDir white',command=get_directoryData,width=10,height=4,bg='red',fg='white')
button.pack()

videoLinkPath=Text(root,width=20 ,height=5,bg='red',fg="white")
videoLinkPath.pack(pady=2)

def downloadVideo():
    global label_path
    global videoLinkPath

root.mainloop()


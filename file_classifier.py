import os
import json
import time
import shutil

import tkinter
import tkinter.filedialog as fl
from tkinter import Tk
Tk().withdraw()

print('Select File Directory You Want To Clean')
path = fl.askdirectory()



def file_lst_txt(path):
    print('txt files')
    newpath = path + '/txt'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print('Folder Created')

    for fle in os.listdir(path):
        if fle.endswith('.txt'):
            print(fle,'txt file')
            #print(path+'/'+fle)
            shutil.move(path+'/'+fle,newpath+'/'+fle)
    
def file_lst_pic(path):
    print('Pictures')
    newpath = path + '/Pictures'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print('Folder Created')

    for fle in os.listdir(path):
        if fle.lower().endswith(('.png', '.jpg', '.jpeg','.svg','.jfif')):
            print(fle)
            shutil.move(path+'/'+fle,newpath+'/'+fle)

def file_lst_docx(path):
    print('Docx')
    newpath = path + '/DOCS'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print('Folder Created')

    for fle in os.listdir(path):
        if fle.lower().endswith('.docx'):
            print(fle)
            shutil.move(path+'/'+fle,newpath+'/'+fle)

def file_lst_pdf(path):
    print('PDF')
    newpath = path + '/PDF'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print('Folder Created')

    for fle in os.listdir(path):
        if fle.lower().endswith('.pdf'):
            print(fle)
            shutil.move(path+'/'+fle,newpath+'/'+fle)

def file_lst_Excel_csv(path):
    print('CSV/Excel')
    newpath = path + '/excel_csv'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        print('Folder Created')

    for fle in os.listdir(path):
        if fle.lower().endswith(('.csv','.xlsx')):
            print(fle)
            shutil.move(path+'/'+fle,newpath+'/'+fle)

file_lst_txt(path)
file_lst_pic(path)
file_lst_docx(path)
file_lst_Excel_csv(path)
file_lst_pdf(path)
print('Cleaned')


#---------#
#from watchdog.observers import Observer
#from watchdog.events import FileSystemEventHandler
#
#class MyHandler(FileSystemEventHandler):
#    i=1
#    def on_modified(self,event):
#        for filename in os.listdir(folder_to_track):
#            src = folder_to_track + "/" + filename
#            os.rename(src,new_destination)
#
#folder_to_track = 'C:/Users/Muneeb/Desktop/track'
#folder_destination = 'C:/Users/Muneeb/Desktop/goto'
#event_handler = MyHandler()
#observer = Observer()
#observer.schedule(event_handler,folder_to_track,recursive=True)
#observer.start()
#
#try:
#    while True:
#        time.sleep(10)
#except KeyboardInterrupt:
#    observer.stop()
#observer.join()
 

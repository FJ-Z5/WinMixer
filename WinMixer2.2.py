from tkinter import *
from tkinter import filedialog, messagebox
from pygame import mixer
import os
from os import sys
import locale
language = str(locale.getdefaultlocale())
Lg=int(language.find("es_"))
if Lg==2:
    Volume_text="Volumen"
    Playing_text="No hay archivos"
    About_text="Acerca de WinMixer"
    File_text="Archivos"
    Contact_text="Contacta al desarrollador"
    Color_text="Modo de color"
    Open_text="Abrir"
    Contact2_text="Contacto"
    Light_text="Modo claro"
    Dark_text="Modo Oscuro"
    OpenFile_text="Abrir un archivo"
    Contact3_text="En GitHub: Fernando-Jelvez/Gmail: fernandojelvez2017@gmail.com"
    AboutInfo_text="WinMixer (Nombre antiguo: F_player) es un reproductor de audio gratis para archivo .mp3 y . wav, desarrollado por Fernando Jelvez, Versión:2.2."
    Error_text="Debes elejir un archivo de audio valido"
    NotSupport_text="Archivo no soportado"
    License_text="Licencia"
else:
    Volume_text="Volume"
    Playing_text="No file"
    About_text="About WinMixer"
    File_text="Files"
    Contact_text="Contact the developer"
    Color_text="Color mode"
    Open_text="Open"
    Contact2_text="Contact"
    Light_text="Light mode"
    Dark_text="Dark mode"
    OpenFile_text="Open a file"
    Contact3_text="On GitHub: Fernando-Jelvez/Gmail:fernandojelvez2017@gmail.com"
    AboutInfo_text="WinMixer (Old name: F_player) is a free music player for .mp3 .and wav files developed by Fernando Jelvez, Version:2.2."
    Error_text="You must choose a valid audio file"
    NotSupport_text="File not supported"
    License_text="License"
LAdvice="""Copyright Fernando Jelves 2020, WinMixer is under the license Apache License v2, If you want to see the rules of the use of WinMiwxer deeper see the web page
http://www.apache.org/licenses/LICENSE-2.0"""
mixer.init()
x = "750"
y = "125"
root = Tk()
root.geometry(x+"x"+y)
root.title("WinMixer Ver.:2.2")
root.resizable(0,0)
root.configure(bg="black")#'#131E3A'
root.iconbitmap("icon.ico")
Color="white"
Fondo="#363636"
Fondo2="black"
currentFile = False
Play=False
DirFiles=""
StopState="Stop"
var=DoubleVar()
Nlista=0
music=0
music1=0
Rep=0
openWindow=0
lista=list(range(0))
lista2=list(range(0))
veces=list(range(0))
vlista3=""
vlista4=""
vlista5=0
V1=2
global From_openWindow
From_openWindow=True
directorio = 0
def Light():
    global Color
    global Fondo
    global Fondo2
    Color="black"
    Fondo="white"
    Fondo2="white"
    root.configure(bg="white")
    botonPlayPause.config(bg=Fondo,fg=Color)
    botonStop.config(bg=Fondo,fg=Color)
    botonNext.config(bg=Fondo,fg=Color)
    botonPrevious.config(bg=Fondo,fg=Color)
    if Rep == 0:
        botonRepeat.config(bg=Fondo,fg=Color)
    elif Rep == -1:
        botonRepeat.config(bg=Fondo)
    w.config(bg=Fondo,fg=Color)
    playing.config(bg=Fondo2,fg=Color)
    VolumeTitle.config(bg=Fondo2,fg=Color)
def Dark():
    global Color
    global Fondo
    global Fondo2
    Color="white"
    Fondo="#363636"
    Fondo2="black"
    root.configure(bg="black")
    botonPlayPause.config(bg=Fondo,fg=Color)
    botonStop.config(bg=Fondo,fg=Color)
    botonNext.config(bg=Fondo,fg=Color)
    botonPrevious.config(bg=Fondo,fg=Color)
    if Rep == 0:
        botonRepeat.config(bg=Fondo,fg=Color)
    elif Rep == -1:
        botonRepeat.config(bg=Fondo)
    w.config(bg=Fondo,fg=Color)
    playing.config(bg=Fondo2,fg=Color)
    VolumeTitle.config(bg=Fondo2,fg=Color)
def aboutShow():
    messagebox.showinfo(title=About_text, message = AboutInfo_text)
def License():
    messagebox.showinfo(title=License_text, message = LAdvice)
def aboutContact():
    messagebox.showinfo(title=Contact2_text, message = Contact3_text)
def openFile():
    if Play==False or StopState=="Pause":
        Stop()
    global lista
    global lista2
    global veces
    lista.clear()
    lista2.clear()
    veces.clear()
    global openWindow
    global currentFile
    global V1
    global vlista5
    global vlista3
    global directorio
    global DirFiles
    vlista5=0
    V1=2
    directorio=0
    vlista3=""
    vlista5=0
    DirFiles=""
    openWindow = filedialog.askopenfilename(title=OpenFile_text,initialdir="/Music", filetypes=(("Audio File","*.mp3;*.wav"),("All files","*.*")))
    currentFile=openWindow
    lista2=openWindow.split("/")
    for x in lista2:
        if not V1 == len(lista2)+1:
            veces.append(lista2[len(lista2)-V1])
            V1=V1+1
    veces.reverse()
    for x in veces:
        directorio=vlista3+veces[vlista5]+"/"
        vlista3=directorio
        vlista5=vlista5+1
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".mp3"):
                 DirFiles=os.path.join(root, file)
                 lista.append(DirFiles)
    for root, dirs, files in os.walk(directorio):
        for file in files:
            if file.endswith(".wav"):
                 DirFiles=os.path.join(root, file)
                 lista.append(DirFiles)
    music=lista.index(openWindow)
    playing.config(text=openWindow)
    From_openWindow=True
menubar = Menu(root)
files = Menu(menubar, tearoff = False)
about = Menu(menubar, tearoff = False)
contact = Menu(menubar, tearoff = False)
Color_mode = Menu(menubar, tearoff = False)
Lisence = Menu(menubar, tearoff = False)
menubar.add_cascade(label = File_text, menu = files)
menubar.add_cascade(label = About_text, menu = about)
menubar.add_cascade(label = Contact_text, menu = contact)
menubar.add_cascade(label = Color_text, menu = Color_mode)
menubar.add_cascade(label = License_text, menu = Lisence)
files.add_command(label = Open_text, command = openFile)
about.add_command(label = About_text, command = aboutShow)
contact.add_command(label = Contact2_text, command = aboutContact)
Color_mode.add_command(label = Light_text, command = Light)
Color_mode.add_command(label = Dark_text, command = Dark)
Lisence.add_command(label = License_text, command = License)
root.config(menu=menubar)
def sel(x):
    global selection
    selection = (var.get()/100)
    mixer.music.set_volume(selection)
def Music():
    global texto4
    newtext.config(text=texto4)
    botonNuevo7.place_forget()
    botonNuevo8.place_forget()
    botonNuevo9.place_forget()
    botonNuevo10.place_forget()
    botonPlay.place(x=375,y=250)
    botonStop.place(x=475,y=250)
    botonPrevious.place(x=575,y=250)
    botonNext.place(x=675,y=250)
    mixer.music.pause()
def PlayPause():
    global Play
    global StopState
    try:
        if Play == False:
            if From_openWindow == True:
                if StopState=="Stop":
                    global music
                    music=lista.index(openWindow)
                    mixer.music.load(currentFile)
                    mixer.music.play(Rep)
                if StopState=="Pause":
                    mixer.music.unpause()
            if From_openWindow == False:
                if StopState=="Stop":
                    mixer.music.load(lista[music])
                    mixer.music.play(Rep)
                if StopState=="Pause":
                    mixer.music.unpause()
            botonPlayPause.config(text=";")
            Play=True
        elif Play == True:
            mixer.music.pause()
            Play=False
            StopState="Pause"
            botonPlayPause.config(text="4")
    except TypeError:
        messagebox.showinfo(title="Error", message = Error_text)
        StopState="Stop"
        Play=False
    except ValueError:
        messagebox.showinfo(title="Error", message = Error_text)
        StopState="Stop"
        Play=False
def Stop():
    mixer.music.pause()
    global Play
    Play=False
    global StopState
    StopState="Stop"
    botonPlayPause.config(text="4")
def Next():
    global From_openWindow
    global music
    From_openWindow=False
    if not music==len(lista):
        music1=music+1
        music=music1
        Prev_Next()
def Previous():
    global From_openWindow
    global music
    From_openWindow=False
    music1=music-1
    music=music1
    Prev_Next()
def Prev_Next():
    if Play == True:
        try:
            mixer.music.load(lista[music])
            mixer.music.play(Rep)
        except:
            messagebox.showinfo(title="Error", message = "File not supported")
    else:
        Stop()
    playing.config(text=lista[music])
def Repeat():
    global Rep
    if Rep == -1:
        Rep=0
        botonRepeat.config(fg=Color)
    elif Rep == 0:
        Rep= -1
        botonRepeat.config(fg="blue")
    mixer.music.pause()
    if Play==True:
        mixer.music.play()

w = Scale(root, from_=0, to=100, orient=HORIZONTAL,variable=var,command=sel,bd=0,relief="solid",bg=Fondo,fg=Color)
w.place(x=550,y=35)
w.set(100)

botonPlayPause= Button(root,bd=1,relief="solid",text="4",font=("Webdings",20),compound="top",command=PlayPause,bg=Fondo,fg=Color)#4=play,;=pause
botonPlayPause.place(x=200,y=30)

botonStop= Button(root,bd=1,relief="solid",text="g",font=("Webdings",15),compound="top",command=Stop,bg=Fondo,fg=Color)
botonStop.place(x=268,y=30)

botonPrevious= Button(root,bd=1,relief="solid",text="9",font=("Webdings",12),compound="top",command=Previous,pady=1,padx=6,bg=Fondo,fg=Color)
botonPrevious.place(x=100,y=30)

botonNext= Button(root,bd=1,relief="solid",text=":",font=("Webdings",12),compound="top",command=Next,pady=1,padx=6,bg=Fondo,fg=Color)
botonNext.place(x=318,y=30)

botonRepeat= Button(root,bd=1,relief="solid",text="q",font=("Webdings",15),compound="top",command=Repeat,bg=Fondo,fg="white")
botonRepeat.place(x=150,y=30)

playing=Label(root,text=Playing_text,font=("Calibri",15,),bg=Fondo2,fg=Color)
playing.place(x=100,y=0)

VolumeTitle=Label(root,text=Volume_text,font=("Calibri",12,),bg=Fondo2,fg=Color)
VolumeTitle.place(x=550,y=75)

root.mainloop()


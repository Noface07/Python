from tkinter import *
from pygame import mixer
from PIL import Image,ImageTk

root=Tk()

root.geometry("700x700+0+0")
root.resizable(0,0)
root.title("Mixer")

root.config(bg="purple")

mixer.init()

def playa():
    mixer.music.load("a.mp3")
    mixer.music.play()
    root.config(bg="purple")
    footer.config(text="Heartless")
    footer2.config(text="Now playing")
def playb():
    mixer.music.load("b.mp3")
    mixer.music.play()
    root.config(bg="purple")
    footer.config(text="Roar")
    footer2.config(text="Now playing")

def playc():
    mixer.music.load("c.mp3")
    mixer.music.play()
    root.config(bg="purple")
    footer.config(text="Dynamite")
    footer2.config(text="Now playing")

def resume():
    mixer.music.unpause()
    root.config(bg="purple")
    footer2.config(text="Now playing")

def pause():
    mixer.music.pause()
    root.config(bg="red")
    footer2.config(text="Paused")

def exit():
    mixer.music.stop()
    root.config(bg="black")
    footer.config(text=" ")
    footer2.config(text="Now playing")


header=Label(root,text="Mixer",font="Arial 20 bold",bd=10,relief=GROOVE)
header.pack(pady=10)

footer = Label(root, text=" ", font="Arial 10 bold", bg="black", fg="Red",
                width="1000",relief="raised",bd="10")  # label is a class
footer.pack(side=BOTTOM , pady=10)

footer2 = Label(root, text="Now playing", font="Arial 10 bold", bg="black", fg="Red",
                width="1000",relief="raised",bd="10")  # label is a class
footer2.pack(side=BOTTOM , pady=10)

btn=Button(root,text="play Song a",command=playa,width=10)
btn.place(x=125,y=300)

btn=Button(root,text="play Song b",command=playb,width=10)
btn.place(x=325,y=300)

btn=Button(root,text="play Song c",command=playc,width=10)
btn.place(x=525,y=300)
# =========================================================

canvas= Canvas(root,width =100, height = 100)
canvas.place(x=110,y=375)

img4=(Image.open("pause.jpg"))

resized_image4 = img4.resize((100,100))
new_image4=ImageTk.PhotoImage(resized_image4)

canvas.create_image(0,0 , anchor=NW, image=new_image4)

# =========================================================
canvas= Canvas(root,width =100 , height = 100)
canvas.place(x=310,y=375)

img5=(Image.open("resume.jpg"))

resized_image5 = img5.resize((100,100))
new_image5=ImageTk.PhotoImage(resized_image5)

canvas.create_image(0,0 , anchor=NW, image=new_image5)

# =============================================================
canvas= Canvas(root,width =100 , height = 100)
canvas.place(x=510,y=375)

img6=(Image.open("stop.jpg"))

resized_image6 = img6.resize((100,100))
new_image6=ImageTk.PhotoImage(resized_image6)

canvas.create_image(0,0 , anchor=NW, image=new_image6)


# ========================================================

btn=Button(root,text="pause",command=pause,width=10)
btn.place(x=125,y=500)

btn=Button(root,text="resume",command=resume,width=10)
btn.place(x=325,y=500)

btn=Button(root,text="exit",command=exit,width=10)
btn.place(x=525,y=500)


# =======================
canvas= Canvas(root, width= 100, height= 100)
canvas.place(x=110,y=175)

#Load an image in the script
img= (Image.open("a.jpg"))

#Resize the Image using resize method
resized_image= img.resize((100,100), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(0,0, anchor=NW, image=new_image)
# =======================

canvas= Canvas(root,width =100 , height = 100)
canvas.place(x=310,y=175)

img2=(Image.open("b.jpg"))

resized_image2 = img2.resize((100,100))
new_image2=ImageTk.PhotoImage(resized_image2)

canvas.create_image(0,0 , anchor=NW, image=new_image2)
# =======================

canvas= Canvas(root,width =100 , height = 100)
canvas.place(x=510,y=175)

img3=(Image.open("c.jpg"))

resized_image3 = img3.resize((100,100))
new_image3=ImageTk.PhotoImage(resized_image3)

canvas.create_image(0,0 , anchor=NW, image=new_image3)
# =========================

photo = PhotoImage(file="a.jpg")

# here, image option is used to
# set image on button



root.mainloop()

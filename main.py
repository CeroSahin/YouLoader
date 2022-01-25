from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as tf


def download():
    var = audio_var.get()
    link = link_entry.get()
    title = title_entry.get()
    try:
        yt = YouTube(link)
    except:
        messagebox.showwarning(
            "Link not found!",
            message="We couldn't find the link you provided. "
                    "Please fill in a YouTube link.")
    else:
        if SAVE_PATH == "no particular path yet!":
            messagebox.showwarning("No Path Specified", message="Please select a path to get the videos downloaded.")
        else:
            # audio only
            if var == 1:
                download_audio(yt)
            # video
            else:
                download_video(yt)


def download_video(yt):
    video = yt.streams.filter(progressive=True, file_extension="mp4").first()
    if video:
        try:
            video.download(output_path=SAVE_PATH, filename=f"{title_entry.get()}.mp4")
            messagebox.showinfo(
                "Success!",
                message="Your video has been downloaded to the path!")
        except:
            messagebox.showwarning("Failure", message="An error occurred during the download process.")
    else:
        messagebox.showinfo("Video not found", message="We couldn't find the video you provided.")
    return


def download_audio(yt):
    audio = yt.streams.filter(only_audio=True, adaptive=True, file_extension="mp4").first()
    if audio:
        try:
            audio.download(output_path=SAVE_PATH, filename=f"{title_entry.get()}.mp4")
            messagebox.showinfo(
                "Success!",
                message="Your audio file has been downloaded to the path!")
        except:
            messagebox.showwarning("Failure", message="An error occurred during the download process.")
    else:
        messagebox.showinfo("Video not found", message="We couldn't find the video you provided.")
    return


def select_path():
    window.directory = tf.askdirectory()
    print(window.directory)
    global SAVE_PATH
    SAVE_PATH = window.directory
    path_label.config(text=SAVE_PATH)
    return


POWDER_BLUE = "#D8E6ED"
SAVE_PATH = "no particular path yet!"


# -------------- GUI LAYOUT ------------------ #
window = Tk()
window.title("YouLoader")
window.minsize(width=600, height=300)
window.config(padx=50, pady=20, bg=POWDER_BLUE)

audio_var = IntVar()

welcome_label = Label(text="Welcome to YouLoader!", font=("Arial", 12), bg=POWDER_BLUE)
welcome_label.grid(column=1, row=0)

subtitle_label = Label(
    text="You can download the YouTube videos\n to your computer with this  application.",
    font=("Arial", 10),
    bg=POWDER_BLUE
)
subtitle_label.grid(column=1, row=1)

link_label = Label(text="Video Link: ", bg=POWDER_BLUE)
link_label.grid(column=0, row=2, sticky="e")

link_entry = Entry(font=("Arial", 10), width=40)
link_entry.grid(column=1, row=2, pady=10)

title_label = Label(text="Write your video title: ", bg=POWDER_BLUE)
title_label.grid(column=0, row=3, sticky="e")

title_entry = Entry(font=("Arial", 10), width=40)
title_entry.grid(column=1, row=3, pady=10)

path_label = Label(text=SAVE_PATH, bg=POWDER_BLUE)
path_label.grid(column=0, row=4, sticky="e")

select_path = Button(text="Select Path", bg="#E7FBBE", command=select_path)
select_path.grid(column=1, row=4, pady=10)

audio_only = Checkbutton(window, text="audio only?", variable=audio_var, onvalue=1, offvalue=0, bg=POWDER_BLUE)
audio_only.grid(columns=1, row=5)

download_button = Button(text="Download", padx=5, pady=5, bg="#e28743", command=download)
download_button.grid(column=1, row=6, pady=10)

window.mainloop()

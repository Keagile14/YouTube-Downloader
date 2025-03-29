import os 
from yt_dlp import YoutubeDL

def download_video(video_url, output_folder="downloads"):

    os.makedirs(output_folder,exist_ok=True)

    options = {
        'format' : 'best',
        'outtmpl':f"{output_folder}/%(title)s.%(ext)s",
        'noplaylist':True,
    }

    try:
        with YoutubeDL(options)as ydl:
            ydl.download([video_url])
        print("\n Download was successful!")
    except Exception as e:
        print(f"\n Error: {e}")
if __name__ == "__main__":
    video_url = input("Enter YouTube Video URL :")
    download_video(video_url)


# import tkinter as tk
# from tkinter import filedialog

# def download_vid(url,save_path):
#     try:
#         yt = YoutubeDL(url)
#         streams = yt.streams.filter(progressive=True,file_extension="mp4")
#         highest_resolution_stream = streams.get_highest_resolution()
#         highest_resolution_stream.download(output_path=save_path)
#         print("Video downloaded successfully!")

#     except Exception as e:
#         print(e)
# url = "https://www.youtube.com/watch?v=xk4_1vDrzzo"
# save_path = "kea@kea-Lenovo-IdeaPad-S145-15IGM"

# download_vid(url,save_path)
from flask import Flask
import subprocess
import json
import youtube_dl


def get_links():
    links = []
    #Read the serialized data from the file
    with open('youtube_links.json', 'r') as file:
        read_data = file.read()
        #Deserialize the JSON data into a list
        links = json.loads(read_data)
    return links


def download():
  save_directory = 'songs'
  youtube_links = get_links()
  list_length = len(youtube_links)
  ytdl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
      'outtmpl': f'{save_directory}/%(title)s.%(ext)s',  # Output template
      'verbose': True
  }
  with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
    for i in range(list_length):
      try:
        ydl.download([youtube_links[i]])
      except Exception as e:
        print("Error downloading: ", youtube_links[i])


def main():
   download()
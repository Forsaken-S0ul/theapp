from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from bs4 import BeautifulSoup
from youtubesearchpython import VideosSearch
import os



app = Flask(__name__)

app.secret_key = "fkasjdffihsgfj"
app.config['SESSION_COOKIE_NAME'] = "mero_cookie"

def load_songs():
   retrieved_list= []
   #Read the serialized data from the file
   with open('ojs_songs.json', 'r') as file:
      read_data = file.read()
   #Deserialize the JSON data into a list
      retrieved_list = json.loads(read_data)
   return retrieved_list 

def load_artists():
   artists = []
   with open('ojs_artists.json','r') as file:
      read_artist = file.read()
      artists = json.loads(read_artist)
   return artists   


def get_link(data):
   link = data['result'][0]['link']
   return link


def search():
   users_songs = load_songs()
   name_of_artist = load_artists()
   number_of_songs = len(users_songs)  
   links = []
   for i in range(number_of_songs):
     query = users_songs[i].replace(" ", "+") + '+' + name_of_artist[i].replace(" ", "+")
     videosSearch = VideosSearch(query , limit = 2)
     response = videosSearch.result()
     link = get_link(response)
     links.append(link)
   
   Links_for_dl = json.dumps(links)
   with open('youtube_links.json','w') as file: 
      file.write(Links_for_dl)


def main():
   search()
   
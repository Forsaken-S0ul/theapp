from flask import Flask, request, url_for, session, redirect
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import time
import spotipy
import json

app = Flask(__name__)

app.secret_key = 'faihgoiqghoieggsjfsg'
app.config['SESSION_COOKIE_NAME'] = 'ojs cookie'
TOKEN_INFO = 'token_info'

def create_spotify_Oauth():
    return SpotifyOAuth(
        client_id='ca3123c4f2c34555be37bd7b0eb8d80d',
        client_secret='bc73636291fb4fea843c0a8fba2c77ed',
        redirect_uri=url_for('redirectPage', _external=True),
        scope='user-library-read'
    )

@app.route('/')
def login():
    sp_oauth = create_spotify_Oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
     sp_oauth = create_spotify_Oauth()
     session.clear()
     code = request.args.get('code')
     token_info = sp_oauth.get_access_token(code)
     session[TOKEN_INFO] = token_info
     return redirect(url_for('getTracks', _external = True))

@app.route("/getTracks")
def getTracks():
   try:
       token_info = get_token()
   except:
       print("user doesn't have the access token")
       redirect(url_for('login', _external = False))
   sp = spotipy.Spotify(auth = token_info['access_token'])
   my_songs = []
   iteration = 0;
   while True:
       items = sp.current_user_saved_tracks(limit = 50, offset = iteration*50)['items']
       iteration+=1
       my_songs += items
       if (len(items)<50):
           break
   list_length = len(my_songs)  
   results = []
   artists_names = []
   for i in range(list_length):
     #helper get all the names of the song from the songs provided by requesting the api
     result = helper(my_songs[i])
     results.append(result)
     # get_artist gets the artist name
     artist = get_artist(my_songs[i])
     artists_names.append(artist)

   serialized_data = json.dumps(results)
   with open('ojs_songs.json','w') as file: 
      file.write(serialized_data)

   serialized_artist = json.dumps(artists_names)
   with open('ojs_artists.json', 'w') as file:
      file.write(serialized_artist)
   return my_songs

def get_token():
    token_info = session.get(TOKEN_INFO,None)
    if not token_info:
        raise Exception("user doesn't have the access token")
    now = time.time()
    is_expired = token_info['expires_at']- now < 60
    if (is_expired):
        sp_oauth = create_spotify_Oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

def helper(song):
    track_name = song['track']['name']
    return track_name  
def get_artist(song):
    artist_name = song['track']['artists'][0]['name']
    return artist_name
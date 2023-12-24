from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

def getTracks(sp):
   my_songs = []
   iteration = 0;
   
   playlist_id = input('enter playlist link(Note: only your own playlists can be downloaded from this):')
   if playlist_id:
    while True:
       items = sp.playlist_tracks(playlist_id,limit = 50, offset = iteration*50)['items']
       iteration+=1
       my_songs += items
       if (len(items)<50):
           break
    else:
      print('please provode a name or id for your playlist.')
   list_length = len(my_songs)  
   results = []
   artists_names = []
   for i in range(list_length):
     #helper get all the names of the song from the songs provided by requesting the api
     result = extract_track_name(my_songs[i])
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


def extract_track_name(song):
    track_name = song['track']['name']
    return track_name  

def get_artist(song):
    artist_name = song['track']['artists'][0]['name']
    return artist_name


def main():
   spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
   getTracks(spotify)
   
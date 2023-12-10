from flask import Flask
import subprocess
import json
import youtube_dl

app = Flask(__name__)

app.secret_key = ";sjfkgakhggklsdgj"
app.config['COOKIE_NAME'] = 'oj_KO_KHANE_KURA'

def link_getter():
    links = []
    #Read the serialized data from the file
    with open('youtube_links.json', 'r') as file:
        read_data = file.read()
        #Deserialize the JSON data into a list
        links = json.loads(read_data)
    return links

@app.route('/')
def index():
    save_directory = '/home/justanoj/ojtheapp/Downloaded_songs'
    youtube_links = link_getter()
    list_length = len(youtube_links)
    try:
      for i in range(list_length):
        subprocess.run(['/home/justanoj/ojtheapp/.venv/bin/youtube-dl', '--audio-format', 'mp3', '-o', f'{save_directory}/%(title)s.%(ext)s', youtube_links[i]])
      return "songs downloaded successfully"
    except Exception as e:
        print(f"Error downloading songs")

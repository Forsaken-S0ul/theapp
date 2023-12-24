# Ojtheapp

## A fully functional project written in python to download your spotify playlists songs

[![GitHub contributors](https://img.shields.io/github/contributors/JustAnOj/ojtheapp)](https://github.com/JustAnOj/ojtheapp/graphs/contributors)

This is a project that was built for solving a common issue for music lovers using python with flask, it lets you download your playlists from spotify.This project leverages the Spotify API to fetch playlist details and downloads the associated tracks.

NOTE:-This program can't download songs youtube-dl doesn't provide

# Features

- **Download Playlists:** Easily download spotify playlists with all the songs that youtube-dl provides.
- **Offline Listening:** Enjoy your favorite music even when you're offline.
- **High-Quality Audio:** Download tracks in the highest available audio quality.

# How to use Ojtheapp

- **_Make a spotify app:_** sign in on the https://developer.spotify.com/ and make a app then copy the client id and secret.
- **_set up environment variable:_** add two environment variables **_SPOTIPY_CLIENT_ID_** **_SPOTIPY_CLIENT_SECRET_**
- **_Clone this repo:_** in the terminal and use the code below:
  `$ git clone https://github.com/JustAnOj/ojtheapp.git`
- **\*install all the dependencies:** in the terminal use the code below:
  `pip install Flask`
  `pip install youtube-dl`
  `pip install youtube-search-python`
- **_run the app and enter the link to your playlist to download:_** in terminal enter the following code to run the program:
  `python3 oj.py`
- **_Enter link to your playlist you want to download:_**the program should prompt you to enter a link to the playlist to download, simply put you playlist's link there and watch the magic happen.

# NOTE:

This is my first project in python so it may contain bugs(very likely). please feel free to contribute to this or make changes or report any bugs. :heart:

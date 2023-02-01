import os
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

with open('apple_playlist.txt', 'r') as f:
    apple_playlist = f.readlines()

song_names = []
for line in apple_playlist:
    track_name, artist_name = line.strip().split(' - ')
    song_names.append(track_name)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = '841ba12129b546c9a100fa42493516fb',
                                                client_secret = 'e256383affd642fc83b09006cfb66d51',
                                                redirect_uri = 'https://open.spotify.com/playlist/44VG7zfGxWTjecpH0w9xv2?si=0097e6804c024ba3',
                                                scope = ["user-library-modify", "playlist-modify-public", "playlist-modify-private"]))

new_playlist_name = input("What is your album name: ")
playlist = sp.user_playlist_create(sp.me()["447e425f45f746b8"], new_playlist_name, public=True)
new_playlist_id = playlist["447e425f45f746b8"]

# Search for each song in the Apple playlist on Spotify and add it to the new Spotify playlist
for song in apple_playlist:
    results = sp.search(q=song, type="track")
    track_id = results["tracks"]["items"][0]["447e425f45f746b8"]
    sp.user_playlist_add_tracks(sp.me()["447e425f45f746b8"], new_playlist_id, [track_id])

print("Transferred Apple playlist to Spotify successfully!")

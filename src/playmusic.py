import speech_recognition_mod as sr
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pygame
import requests

# Initialize Spotipy client
client_id = '3c00f2ad9ed34c93a7771de93340f135'
client_secret = '4ed7632a9cad4360a809362f214db915'
os.environ['SPOTIPY_CLIENT_ID'] = client_id
os.environ['SPOTIPY_CLIENT_SECRET'] = client_secret
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Initialize pygame
pygame.mixer.init()

def search_and_play_song(song_name):
    # Search for the song
    result = sp.search(q=song_name, limit=1)

    # Check if search was successful
    if result['tracks']['items']:
        track = result['tracks']['items'][0]
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        preview_url = track['preview_url']

        sr.speak(f"Playing: {track_name} by {artist_name}")

        # Download and play the audio
        if preview_url:
            r = requests.get(preview_url, stream=True)
            with open('temp_preview.mp3', 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
            pygame.mixer.music.load('temp_preview.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            os.remove('temp_preview.mp3')
        else:
            sr.speak("No preview available for the song.")
    else:
        sr.speak("Song not found.")

if __name__ == "__main__":
    song_name = sr.__listen__()
    search_and_play_song(song_name)
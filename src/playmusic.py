import requests

# Load Deezer API credentials


# Search for a song on Deezer
def search_song(song_name):
    client_id=''
    client_secret=''

    # Get access token
    access_token = get_access_token(client_id, client_secret)
    if not access_token:
        print("Failed to obtain access token.")
        return

    # Search for the song
    url = f"https://api.deezer.com/search?q={song_name}"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and data['data']:
            song = data['data'][0]  # Retrieve the first song
            print(f"Song found: {song['title']} by {song['artist']['name']}")
            return song['preview']
        else:
            print("Song not found.")
    else:
        print("Error:", response.status_code)

# Get access token for Deezer API
def get_access_token(client_id, client_secret):
    url = "https://connect.deezer.com/oauth/access_token.php"
    payload = {
        "app_id": client_id,
        "secret": client_secret,
        "output": "json",
        "type": "client_credentials",
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        data = response.json()
        if 'access_token' in data:
            return data['access_token']
    return None

if __name__ == "__main__":
    song_name = input("Enter the name of the song: ")
    preview_url = search_song(song_name)
    if preview_url:
        print("Preview URL:", preview_url)
    else:
        print("Preview not available for the song.")

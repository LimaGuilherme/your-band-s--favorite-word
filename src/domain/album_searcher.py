import spotipy

from typing import List
from spotipy.oauth2 import SpotifyClientCredentials

from src import configurations as config_module

config = config_module.get_config()


class AlbumsSearcher:

    def __init__(self):
        client_credentials_manager = SpotifyClientCredentials(client_id=config.SPOTIFY_CLIENT_ID,
                                                              client_secret=config.SPOTIFY_CLIENT_SECRET)
        self.__spotify_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def remove_remaster_and_live_albums(self, albums: List[str]) -> List[str]:
        acceptable_albums = []
        unacceptable_albums = ['instrumental', 'international', 'live', 'version',
                               'limited', 'mtv', 'bonus', 'tour', 'anniversary', 'standard', 'track',
                               'exclusive', 'gold', 'edition', 'commentary', 'remaster', 'acoustic']
        for album in albums:
            this_album_album_is_acceptable = True
            album = album.replace('(', '')
            album = album.replace(')', '')

            album_title = album.split(sep=" ")

            for album_tittles in album_title:
                if album_tittles.lower() in unacceptable_albums:
                    this_album_album_is_acceptable = False
                    break

            if this_album_album_is_acceptable:
                acceptable_albums.append(album)

        return acceptable_albums

    def get_albums(self, artist: str) -> List[str]:
        results = self.__spotify_client.search(q="artist:" + artist, type="artist")
        items = results["artists"]["items"]

        if not items:
            return []

        artist_item = items[0]

        albums = []
        albums_titles = []
        results = self.__spotify_client.artist_albums(artist_item["id"],
                                                      album_type="album")
        albums.extend(results["items"])

        while results["next"]:
            results = self.__spotify_client.next(results)
            albums.extend(results["items"])
        seen = set()
        albums.sort(key=lambda album: album["name"].lower())

        for album in albums:
            album_tittle = album["name"]

            if album_tittle not in seen:
                print(" " + album_tittle)
                seen.add(album_tittle)
                albums_titles.append(album_tittle)
        return albums_titles

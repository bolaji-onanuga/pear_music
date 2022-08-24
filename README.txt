Description:

Downloader tool for apple music songs and playlists.
Allows DJs to collect and share music more easily.

Uses regex to search for songs using youtube-dl dependency, downloading
them in m4a format.


Steps/Algorithm/MOSCOW

0. Pass song or playlist URL via command line/read in playlist txt file exported from iTunes
    # may require re-saving text file in UTF-8 format.

1. Get titles and artists of song, or songs in playlist, using Apple Music API
    1.5 Use applemusicpy Python API wrapper to simplify things
    1b. AM API needs dev license (£79). Instead use text playlist export, cleaned with regex to search youtube-dl.

2. Pass title(s)/artist(s) to search youtube-dl to download each song in m4a format



Stretch Goals:
- Fill out song metadata.
- Skip downloading songs I already have by deleting lines 
that aren't Apple Music AAC files from result regex.
- Artwork for each song
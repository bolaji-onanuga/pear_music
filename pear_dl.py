import os
from youtube_dl import YoutubeDL
import re
import subprocess

os.chdir("G:\Music\Apple Rips")

fp = "UKG_FUNKY_D&B_2 STEP_GRIME.txt"  #Read in txt playlist exported from itunes.
with open(fp, 'r', encoding='utf=8') as f:
    list = f.read()
    # may require may require opening and re-saving text file in UTF-8 format if you get UnicodeDecodeError

os.chdir("G:\Music\Apple Rips")

# replace weird spaces with commas
regex = r"	"
subst = ","
result = re.sub(regex, subst, list, 0, re.MULTILINE)

# Remove songs that arent this filetype, as we already have them
reg = r"^(?!.*Apple Music AAC audio file.*).+$"
subst = ""
result = re.sub(reg,subst,result,0, re.MULTILINE)

if result:

    # get song titles & artist names using regex
    title_artists = re.findall(r"^([^,]*,)([^,]*,)", result, re.MULTILINE)

    # use yt-dl to search each title/artist pair, dling 1st result
    for title_artist in title_artists:
       t_a_str = ' '.join(title_artist)
       t_a_str = re.sub(",","",t_a_str)

       print("Now Downloading: " + t_a_str + "\n") 
       query = "ytsearch1:"  + t_a_str.strip()
       subprocess.run(["youtube-dl", query, "-f", "m4a"])
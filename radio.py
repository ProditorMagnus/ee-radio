#!/usr/bin/python3

import urllib.request
import datetime
import json

# to improve: check timestamp, and if too old raise some notice somewhere
folder = "/home/ravana/python/radio/out/"

try:
	with open(folder + "starfm.txt", "a", encoding="utf8") as myfile:
		data = json.loads(urllib.request.urlopen("http://rds.starfm.ee/jsonRdsInfo.php?Name=Star", None, 2).read().decode('utf-8')[1:-1])
		myfile.write(('{:%d.%m.%Y %H:%M:%S}'.format(datetime.datetime.now())+" "+data["currentArtist"]+" - "+data["currentSong"]))
		myfile.write("\n")
except Exception as e:
	print(e)
	pass
try:
	with open(folder + "ringfm.txt", "a", encoding="utf8") as myfile:
		myfile.write(('{:%d.%m.%Y %H:%M:%S}'.format(datetime.datetime.now())+" "+json.loads(urllib.request.urlopen("http://www.ringfm.ee/ajax/action/updateOnAir/", None, 2).read().decode('utf-8'))["on_air_now"]))
		myfile.write("\n")
except Exception as e:
	print(e)
	pass
try:
	with open(folder + "hitfm.txt", "a", encoding="utf8") as myfile:
		myfile.write(('{:%d.%m.%Y %H:%M:%S}'.format(datetime.datetime.now())+" "+json.loads(urllib.request.urlopen("http://stream.akaver.com/songtitles/get_jsonp.php?file=hitfm", None, 2).read().decode('utf-8'))["artist_title"]))
		myfile.write("\n")
except Exception as e:
	print(e)
	pass
# with open("retrofm.txt", "a", encoding="utf8") as myfile:
	# myfile.write(('{:%d.%m.%Y %H:%M:%S}'.format(datetime.datetime.now())+" "+json.loads(urllib.request.urlopen("http://stream.akaver.com/songtitles/get_jsonp.php?file=retrofm", None, 2).read().decode('utf-8'))["artist_title"]))
	# myfile.write("\n")
try:
	with open(folder + "retrofm.txt", "a", encoding="utf8") as myfile:
		data = json.loads(urllib.request.urlopen("http://dad.akaver.com/api/SongTitles/RETRO", None, 2).read().decode('utf-8'))
		myfile.write(('{:%d.%m.%Y %H:%M:%S}'.format(datetime.datetime.now())+" "+data["SongHistoryList"][0]["Artist"]+" - "+data["SongHistoryList"][0]["Title"]))
		myfile.write("\n")
except Exception as e:
	print(e)
	pass

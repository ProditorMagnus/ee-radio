#!/usr/bin/python3
import datetime
import json
import urllib.request

def get(folder, fileName, stationId):
    try:
        with open(folder + "/" + fileName + ".txt", "a", encoding="utf8") as myfile:
            data = json.loads(urllib.request.urlopen("http://dad.akaver.com/api/SongTitles/" + stationId, None, 2).read().decode('utf-8'))
            song = data["SongHistoryList"][0]
            myfile.write(('{:%d.%m.%Y %H:%M:%S}'.format(datetime.datetime.utcfromtimestamp(song["TimeStamp"]))+" "+song["Artist"]+" - "+song["Title"]))
            myfile.write("\n")
    except Exception as e:
        print(e)
        pass


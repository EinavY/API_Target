# -*- coding: utf-8 -*-
"""
Created on Thu May 13 08:37:09 2021

@author: Einav
"""
import requests
import smtplib
import json
api_file = open("api.txt", "r")
api_key = api_file.read()
api_file.close()
dests_file = open("dests.txt", "r", encoding="utf-8")
source = "תל%אביב"
city_dic = dict()
dis_dic = dict()
countCity = 1
##find the distance, time, lng and lat from tlv to any target
## the size of dictionary of targets is 5 only
for line in dests_file:
    if countCity >5:
        break
    target = line
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"
    r = requests.get(url + "origins=" + source + "&destinations=" + target + "&key=" + api_key)
    if r.json()["rows"][0]["elements"][0]["status"] == "NOT_FOUND":
        city_dic[target] = ("The place is not exist")
    else:
        time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
        distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
        url2 = "https://maps.googleapis.com/maps/api/geocode/json?"
        r2 = requests.get(url2 + "address=" + target + "&key=" + api_key)
        results = r2.json()['results']
        lat = results[0]['geometry']['location']['lat']
        lng = results[0]['geometry']['location']['lng']
        city_dic[target] = ("distance from tlv:", distance,"time from tlv:", time,"Longitude of the target:", lng, "Latitude of the target:", lat)
        dis_dic[target] = distance
    countCity = countCity+1
##print the dictionary
print("A dictionary that contains geographical information of 5 cities in relation to Tel Aviv:")
print()
print(city_dic)
print()
print()
## print the data from dictionary
for target, distance in city_dic.items():
    print("Geographical information of each city in relation to Tel Aviv:")
    print()
    print(target, distance)
print()
print()
##Finding the 3 cities furthest from Tel Aviv
print("The 3 cities furthest from Tel Aviv:")
print()
length_distance = sorted(dis_dic.items(), key=lambda x: x[1], reverse=True)
i = 1
for dis in length_distance:
    print(dis[0], dis[1])
    i = i+1
    if i >3:
        break









        






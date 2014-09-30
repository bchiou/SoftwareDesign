# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 14:27:39 2014

@author: brandon

access_token ='CAACEdEose0cBAPvWaePglq98cidVoxXVMDMSL33NhR36PZBCSzZBgiIac0nE46EZCafJTBtXxhIFog2r3k4myIiFm5ZBBirvXupUzgEnWZBqDhULKITChLTs1aBeqI0MZBdKKVnYJIQ9T7YjwDQN1EsQWLrRKUgzxQr0AKZAxNwgHWZC5hLnYNNO8rMFvccOAmPNs4zcKnqZCEsiH2PbZASY8weNz359s3XVQZD'
"""

import urllib2
import json

access_token = raw_input('What is your access token?\n')
retrieved = int(raw_input('How many messages do you want retrieved?\n'))

def getMessages(url, messages):
    connection = urllib2.urlopen(url) #assigns file-like object given above 'url' to 'connection'
    html = connection.read() #assigns url to html
    my_feed = json.loads(html) #json parses url content (HTML) into dictionary
    count1 = 0
    for feed in my_feed["data"]:
        if "message" in feed and "#" in feed["message"]:
            count1 +=1
            messages.append(feed["message"])
            print feed["message"] + "\n" #only prints messages with #

    print "Number of messages with #: %d" % count1
    return my_feed["paging"]["next"]

if __name__ == "__main__":
    #access_token ='CAACEdEose0cBAPvWaePglq98cidVoxXVMDMSL33NhR36PZBCSzZBgiIac0nE46EZCafJTBtXxhIFog2r3k4myIiFm5ZBBirvXupUzgEnWZBqDhULKITChLTs1aBeqI0MZBdKKVnYJIQ9T7YjwDQN1EsQWLrRKUgzxQr0AKZAxNwgHWZC5hLnYNNO8rMFvccOAmPNs4zcKnqZCEsiH2PbZASY8weNz359s3XVQZD'
    url = "https://graph.facebook.com/v2.1/me/home?access_token=" + access_token #url beginning + user id
    
    total_messages = [] #total messages accessed from feed
    count2 = 0
    while(len(total_messages)< retrieved):
        print "Accessed Facebook %d times" % count2 + "\n" 
        url = getMessages(url, total_messages)
        count2 += 1
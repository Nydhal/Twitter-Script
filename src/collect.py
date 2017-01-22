import time
import tweepy  # https://github.com/tweepy/tweepy
import csv
import sys

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

# Twitter API credentials, check ceredentials file for credential if empty prompt user
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Construct the API instance
api = tweepy.API(auth)

# Specify I/O files
inputfile = 'userlist.txt'
outputfile = 'resultlist.txt'

#Initialize Result file
with open(outputfile, "wt") as out_file:
	out_file.write("id,date,friends,followers,IsProtected\n")

# Read ids from textfile, load into list (idlist[0]='id') and print list length
idlist = [line.strip('\n') for line in open(inputfile)]

idlist.pop(0) #remove 'id'

listlen = len(idlist)
print("userlist length is :",listlen)

# Partition list into ngrp groups of <=100
partidlist = [idlist[x:x+100] for x in range(0, listlen, 100)]
ngrp = len(partidlist)
print("number of groups :",ngrp)


#search
if __name__ == '__main__':

	for i in range(0,ngrp):

			# API Call to get a group (~100 users) status
			currentgroup = api.lookup_users(partidlist[i]) #user list length API limit = 100
			print("\n Starting Group : ",i+1,'\n')

			for index, user in enumerate(currentgroup):
				
				# Console output
				print ("---------------------------------",i,index+1)
				print ("ID :",user.id)
				print ("screen name   : @",user.screen_name)
				print ("username        :",user.name)
				print ("Creation Date   :",user.created_at)
				print ("friends_count   :",user.friends_count)
				print ("followers_count :",user.followers_count)    
				print ("Is protected?   :",user.protected)

				# Format then wrtie result to file
				line = str(user.id)+','+str(user.created_at)+','+str(user.friends_count)+','+str(user.followers_count)+','+str(user.protected)+'\n'
				with open(outputfile, 'a') as out_file:
					out_file.write(line) 

	

# Check Rate Limits
data = api.rate_limit_status()
print (data['resources']['statuses']['/statuses/home_timeline'])
print (data['resources']['users']['/users/lookup'])

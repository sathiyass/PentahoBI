import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

import httplib2
import os
import re
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

import urllib
import json

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the {{ Cloud Console }}
{{ https://cloud.google.com/console }}

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))
								   
# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

CHANNEL_ID=''

def get_authenticated_service():
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPES,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("%s-oauth2.json" % sys.argv[0])
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage)

  return build(API_SERVICE_NAME, API_VERSION,
    http=credentials.authorize(httplib2.Http()))
	
def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyClzZA1w4oTBHA_w5NVZJMgAuOQI74GqPE'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=5'.format(api_key, channel_id)
    first_url="https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PLYHulBl0AWQA-2D-TAKYbqcqu06QjIEWr&key=AIzaSyClzZA1w4oTBHA_w5NVZJMgAuOQI74GqPE"
    print(first_url);
    video_links = []
    video_ids = []
    url = first_url
    while True:
        inp = urllib.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])
                video_ids.append(i['id']['videoId'])
        try:
            break		
            next_page_token = resp['nextPageToken']
            #print next_page_token
            url = first_url + '&pageToken={}'.format(next_page_token)
            #print url
        except:
            print "Video links fetched, Nextpagetoken doesn't Exist."
            break
	
	# Writing the data to txt file in current directory
    data = open("VideolistbyChannel.txt", "w")
	
    for links in video_links:	  
            data.write("%s\n" % (links))
    data.close()
	
    return video_ids
	
def get_all_playlist_in_channel(channel_id):
    api_key = 'AIzaSyClzZA1w4oTBHA_w5NVZJMgAuOQI74GqPE'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/playlists?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,contentDetails&maxResults=5'.format(api_key, channel_id)
    first_url="https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=PLYHulBl0AWQA-2D-TAKYbqcqu06QjIEWr&key=AIzaSyClzZA1w4oTBHA_w5NVZJMgAuOQI74GqPE"
    #print(first_url);
    playlist_links = []
    playlist_ids = []
    url = first_url
    while True:
        inp = urllib.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#playlist":
                #video_links.append(base_video_url + i['id']['videoId'])
                playlist_ids.append(i['id'])
        try:            
            next_page_token = resp['nextPageToken']
            #print next_page_token
            url = first_url + '&pageToken={}'.format(next_page_token)
            #print url
        except:
            print "PL links fetched, Nextpagetoken doesn't Exist."
            break
	
	# Writing the data to txt file in current directory
    data = open("PlaylistsbyChannel.txt", "w")
	
    for links in playlist_ids:	  
            data.write("%s\n" % (links))
    data.close()
	
    return playlist_ids

def channels_list_by_username(service, **kwargs):
  results = service.channels().list(
    **kwargs
  ).execute()
  
  CHANNEL_ID=results['items'][0]['id']
  print('Channel ID: '+results['items'][0]['id'])
  print('Title: '+results['items'][0]['snippet']['title'])	
  print('Total Number of views: '+results['items'][0]['statistics']['viewCount'])
  return results

def print_response(response):
  print(response)

# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
  resource = {}
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]

      # For properties that have array values, convert a name like
      # "snippet.tags[]" to snippet.tags, and set a flag to handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True

      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        # For example, the property is "snippet.title", but the resource does
        # not yet have a "snippet" object. Create the snippet object here.
        # Setting "ref = ref[key]" means that in the next time through the
        # "for pa in range ..." loop, we will be setting a property in the
        # resource's "snippet" object.
        ref[key] = {}
        ref = ref[key]
      else:
        # For example, the property is "snippet.description", and the resource
        # already has a "snippet" object.
        ref = ref[key]
  return resource

# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs
 
def videos_list_by_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.videos().list(
    **kwargs
  ).execute()

  #return print_response(response)
  return response
if __name__ == '__main__':
	  
  CHANNEL_ID='UCuxc7jait6qV6i70cMp7Erw'
  
  # Passing the channel ID to get all the videos list
  # Limitations: max of 500 videos will be extracted from the channel,
  
  video_ids=get_all_video_in_channel(CHANNEL_ID) # Input is the channel ID
#!/usr/bin/python

###
#
# Retrieves YouTube Analytics report data. The script's default behavior
# is to retrieve data for the authenticated user's channel. However, if you
# set a value for the --content-owner command-line argument, then the script
# retrieves data for that content owner. Note that the user running the script
# must be authorized to retrieve data for that content owner.
#
# Note that when you retrieve Analytics data for a content owner, your API
# request must set a value for the "filters" request parameter as explained
# in the API documentation here:
# https://developers.google.com/youtube/analytics/v1/content_owner_reports#Filters
#
# By default, if you set a value for the --content-owner argument, then the
# "filters" parameter is set to "claimedStatus==claimed". (On the other hand,
# this value is not set if you are retrieving data for your own channel.)
#
# You can use the --filters command-line argument to set the "filters" parameter
# for any request. For example:
#   * --filters="channel==CHANNEL_ID"
#   * --filters="channel==CHANNEL_ID;country==COUNTRY_CODE"
#   * --filters="video==VIDEO_ID"
#   * --filters="claimedStatus==claimed;uploaderType==thirdParty"
#   * etc.
#
###

import argparse
import os
import httplib2
import re
import sys
import json

import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta


from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import ConfigParser

Config_dir="/informatica/ia2/MMRGROUP/MMR-Coop/tools/apache-tomcat-7.0.70/webapps/python/youtubeapi/data-api/config"
SettingsConfigFile="settings.config"

config = ConfigParser.ConfigParser()
config.readfp(open(r''+Config_dir+'/'+SettingsConfigFile+''))

scripts_dir = config.get('dir-config', 'scripts_dir')
keys_dir = config.get('dir-config', 'keys_dir')
reports_dir = config.get('dir-config', 'reports_dir')


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the {{ Google Cloud Console }} at
# {{ https://cloud.google.com/console }}.
# Please ensure that you have enabled the YouTube Analytics API for your project.
# For more information about using OAuth2 to access the YouTube Analytics API, see:
#   https://developers.google.com/youtube/reporting/guides/authorization
# For more information about the client_secret.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
#CLIENT_SECRETS_FILE = 'client_secret.json'


# These OAuth 2.0 access scopes allow for read-only access to the authenticated
# user's account for both YouTube Data API resources and YouTube Analytics Data.
SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']
API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v1'

# Authorize the request and store authorization credentials.
#def get_authenticated_service():
#  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#  credentials = flow.run_console()

#  api_service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
#  return api_service

def get_authenticated_service(CLIENT_SECRETS_FILE,CLEINT_OAUTH_FILE):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=SCOPES,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage(CLEINT_OAUTH_FILE)
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage)

  return build(API_SERVICE_NAME, API_VERSION,
    http=credentials.authorize(httplib2.Http()))
	
# Remove keyword arguments that are not set.
def remove_empty_args(args):
  original_args = vars(args)
  good_args = {}
  if original_args is not None:
    for key, value in original_args.iteritems():
      # The channel_id and content_owner arguments are provided as a means
      # of properly setting the "ids" parameter value. However, they should
      # not be included in the API request (since they're not parameters
      # supported by this method).
      if value and key != 'channel_id' and key != 'content_owner':
        good_args[key] = value
  return good_args
  
# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs

# Set the "ids" request parameter for the YouTube Analytics API request.
def set_ids_parameter(args):
  if args.content_owner:
    args.ids = 'contentOwner==' + args.content_owner
    if args.filters == '':
      args.filters = 'claimedStatus==claimed'
  elif args.channel_id:
    args.ids = 'channel==' + args.channel_id
  else:
    args.ids = 'channel==MINE'
  args = remove_empty_args(args)
  print args
  return args
  
def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyClzZA1w4oTBHA_w5NVZJMgAuOQI74GqPE'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=5'.format(api_key, channel_id)

    #print(first_url);
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
	
def run_analytics_report(youtube_analytics, args, report_feed):
  # Call the Analytics API to retrieve a report. Pass args in as keyword
  # arguments to set values for the following parameters:
  #
  #   * ids
  #   * metrics
  #   * dimensions
  #   * filters
  #   * start_date
  #   * end_date
  #   * sort
  #   * max_results
  #
  # For a list of available reports, see:
  # https://developers.google.com/youtube/analytics/v1/channel_reports
  # https://developers.google.com/youtube/analytics/v1/content_owner_reports
  analytics_query_response = youtube_analytics.reports().query(
    **args
  ).execute()

  #print 'Analytics Data for Channel %s' % channel_id
  
  print analytics_query_response
  
  with open(report_feed,'w') as outfile:
    json.dump(analytics_query_response, outfile)
  
  #for column_header in analytics_query_response.get('columnHeaders', []):
  #  print '%-20s' % column_header['name'],
  #print
  
	
  #for row in analytics_query_response.get('rows', []):
  #  for value in row:
  #    print '%-20s' % value,
  #  print

def channels_list_by_id(client, **kwargs):
  # See full sample for function
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.channels().list(
    **kwargs
  ).execute()

  return print_response(response)
  
if __name__ == '__main__':
  now = datetime.now()
  one_day_ago = (now - timedelta(days=1)).strftime('%Y-%m-%d')
  one_week_ago = (now - timedelta(days=7)).strftime('%Y-%m-%d')

  parser = argparse.ArgumentParser()

  # Set channel ID or content owner. Default is authenticated user's channel.
  parser.add_argument('--channel-id', default='',
      help='YouTube channel ID for which data should be retrieved. ' +
           'Note that the default behavior is to retrieve data for ' +
           'the authenticated user\'s channel.')
  parser.add_argument('--content-owner', default='',
      help='The name of the content owner for which data should be ' +
           'retrieved. If you retrieve data for a content owner, then ' +
           'your API request must also set a value for the "filters" ' +
           'parameter. See the help for that parameter for more details.')

  # Metrics, dimensions, filters
  parser.add_argument('--metrics', help='Report metrics',
    default='views,estimatedMinutesWatched,averageViewDuration')
  parser.add_argument('--dimensions', help='Report dimensions', default='')
  parser.add_argument('--filters', default='',
      help='Filters for the report. Note that the filters request parameter ' +
           'must be set in YouTube Analytics API requests for content owner ' +
           'reports. The script sets "filters=claimedStatus==claimed" if a ' +
           'content owner is specified and filters are not specified.')

  # Report dates. Defaults to start 7 days ago, end yesterday.
  parser.add_argument('--start-date', default=one_week_ago,
    help='Start date, in YYYY-MM-DD format')
  parser.add_argument('--end-date', default=one_day_ago,
    help='End date, in YYYY-MM-DD format')

  parser.add_argument('--max-results', help='Max results')
  parser.add_argument('--sort', help='Sort order', default='')
  parser.add_argument('--alt', default='json',
      help='Data Format')
  parser.add_argument('--owner', help='owner is required for authorization of the ContentOwner Channels', required=True)
  parser.add_argument('--feed', default='content.json',
      help='JSON Data')
  args = parser.parse_args()
  args = set_ids_parameter(args)
  
  
  #print args['contentOwner']
  #print len(sys.argv)
  OWNER=args['owner']
  CLIENT_SECRETS_FILE=keys_dir+'/client_secret_'+OWNER+'.json'
  CLEINT_OAUTH_FILE=keys_dir+'/'+os.path.basename(sys.argv[0])+'-oauth2_'+OWNER+'.json'
  API_KEY=config.get('apikey-config','api_key_'+OWNER)
  
  print CLIENT_SECRETS_FILE
  print CLEINT_OAUTH_FILE
  print API_KEY
  #print sys.argv[len(sys.argv)-1]
  
  report_feed=args['feed']
  
  del args['owner']
  del args['feed']
  
  
  MISSING_CLIENT_SECRETS_MESSAGE = """
    WARNING: Please configure OAuth 2.0

    To make this code run you will need to populate the client_secrets_{owner}.json file
    found at:

    %s

    with information from the {{ Cloud Console }}
    {{ https://cloud.google.com/console }}

    For more information about the client_secrets.json file format, please visit:
    https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
    """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))
								   
  youtube_analytics = get_authenticated_service(CLIENT_SECRETS_FILE,CLEINT_OAUTH_FILE)
  
  try:
    run_analytics_report(youtube_analytics, args, report_feed)
	#channels_list_by_id(youtube_analytics,part='snippet,contentDetails,statistics',id='UC_x5XG1OV2P6uZZ5FSM9Ttw')
  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
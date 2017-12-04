import urllib
import json


def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyClzZA1w4oTBHA_w5NVZJMgAuOQI74GqPE'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=50'.format(api_key, channel_id)

    print(first_url);
    video_links = []
    url = first_url
    while True:
        inp = urllib.urlopen(url)
        print inp.read()
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            print next_page_token
            url = first_url + '&pageToken={}'.format(next_page_token)
            print url
        except:
            print "Error"
            break
			
    return video_links
	
    

        
	
video_links=get_all_video_in_channel('UClUsCEaF7EkbNFLBOwjCK8w')

#a_merged = ' '.join(video_links)
#with open("Videos.txt",'w') as f:
#    f.write(a_merged)
	
data = open("list.txt", "w")
for c in video_links:
    data.write("%s\n" % (c))
data.close()
	
#print len(video_links)
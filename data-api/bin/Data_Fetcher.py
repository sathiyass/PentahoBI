import subprocess
import os
import sys
import ConfigParser

Config_dir="/informatica/ia2/MMRGROUP/MMR-Coop/tools/apache-tomcat-7.0.70/webapps/python/youtubeapi/data-api/config"
SettingsConfigFile="settings.config"

config = ConfigParser.ConfigParser()
config.readfp(open(r''+Config_dir+'/'+SettingsConfigFile+''))

path = config.get('dir-config', 'scripts_dir')
path2 = config.get('dir-config', 'keys_dir')
path3 = config.get('dir-config', 'reports_dir')
	
if __name__ == '__main__':
	
	
    print path
	
    #os.system("python "+path+"yt_analytics_report.py --metrics=views,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCuxc7jait6qV6i70cMp7Erw' --start-date=2017-11-03 --end-date=2017-12-03 --feed=LATAM_BoomerangBrasil_AllData_Monthly.json")
    os.system("python "+path+"/yt_analytics_report.py --metrics=views,comments,likes,dislikes,videosAddedToPlaylists,videosRemovedFromPlaylists,shares,estimatedMinutesWatched,estimatedRedMinutesWatched,averageViewDuration,averageViewPercentage,annotationClickThroughRate,annotationCloseRate,annotationImpressions,annotationClickableImpressions,annotationClosableImpressions,annotationClicks,annotationCloses,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCuxc7jait6qV6i70cMp7Erw;video==Lmo4rC_Ocl8' --start-date=2017-11-03 --end-date=2017-12-03 --owner=latam --feed=LATAM_BoomerangBrasil_AllData_Monthly.json")
	
    #os.system("python "+path+"yt_analytics_report.py --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCuxc7jait6qV6i70cMp7Erw' --dimensions=playlist --feed=LATAM_Country_Weekly.json")
	
	# Fetching Total views, subscribersGained, subscribersLost, Country, SourceType of a channel from channel creation date
	
      #os.system("python "+path+"yt_analytics_report.py --metrics=views,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCuxc7jait6qV6i70cMp7Erw' --start-date=1995-11-01 --end-date=2017-12-02 --feed=LATAM_BoomerangBrasil_AllChannelData.json")
	
    #os.system("python "+path+"yt_analytics_report.py --metrics=views,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCuxc7jait6qV6i70cMp7Erw' --start-date=1995-11-01 --end-date=2017-12-30 --feed=LATAM_BoomerangBrasil_AllChannelData.json")
	
      #os.system("python "+path+"yt_analytics_report.py --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCuxc7jait6qV6i70cMp7Erw' --dimensions=country --start-date=1995-11-01 --end-date=2017-11-30 --feed=LATAM_Country_Weekly.json")

      #os.system("python "+path+"yt_analytics_report.py --metrics=views,estimatedMinutesWatched --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCuxc7jait6qV6i70cMp7Erw' --dimensions=insightTrafficSourceType --start-date=1995-11-01 --end-date=2017-11-30 --feed=LATAM_SourceType_Weekly.json")
	
	
	
    #os.system("python "+path+"yt_analytics_report.py --metrics=videosAddedToPlaylists,videosRemovedFromPlaylists --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --start-date=1995-11-01 --end-date=2017-11-30 --feed=LATAM_Videorep.json")
    #os.system("python yt_analytics_report.py --metrics=views --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='isCurated==1;channel==UCuxc7jait6qV6i70cMp7Erw' --dimensions=playlist --max-results=100 --start-date=2015-11-01 --end-date=2017-12-01 --sort=-views --feed=LATAM_Top10Videos_AllData_Monthly.json")
   
import subprocess
import os
import sys


if __name__ == '__main__':

   print "Fetching Monthly Data for LATAM Content Owner.."
   
   #### Total # of Videos viewed (Total views + User generated content) for the given ContentOwner Monthly ####
   
   os.system('python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_contentOwnerAllData_Monthly.json')
  
   os.system('python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters=claimedStatus==claimed --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_contentOwnerClaimedData_Monthly.json')
   
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='claimedStatus==claimed;uploaderType==self' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_ClaimedSelfUploadData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='claimedStatus==claimed;uploaderType==thirdParty' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_ClaimedThirdPartyData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='uploaderType==self' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_SelfUploadData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='uploaderType==self' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_SelfUploadData_Monthly.json")
   
   
   #### Total # of Video Views across LATAM Kids Channels ####
   print "Fetching channel wise Monthly data for LATAM Content Owner Channels.."
   
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCuxc7jait6qV6i70cMp7Erw' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_BoomerangBrasil_AllData_Monthly.json")
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCqc73wuwWpRMHPL_mmtAZAQ' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_BoomerangLA_AllData_Monthly.json")
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCkC6Pr-IGe7xmFyjdfsV1dg' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_StevenUniverseLA_AllData_Monthly.json")
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UC3IIbdGzO_8TqqNDzUR-gBg' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_StevenUniverseBrasil_AllData_Monthly.json")
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UCQySZQ6rrgJXRuonMwIIGMA' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_CarttonNetworkLA_AllData_Monthly.json")
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='channel==UC1toK6UDXwreacdepXYcyqA' --start-date=2017-11-01 --end-date=2017-11-30 --feed=LATAM_CarttonNetworkBrasil_AllData_Monthly.json")
   
   
   #### Total # of Video Views across LATAM Kids Channels ####
   print "Fetching COUNTRY wise Monthly data for LATAM Content Owner.."
   
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=country --feed=LATAM_CountryDim_AllData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='uploaderType==self;claimedStatus==claimed' --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=country --feed=LATAM_CountrySelfClaimed_AllData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='uploaderType==thirdParty;claimedStatus==claimed' --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=country --feed=LATAM_CountryThirdPartyClaimed_AllData_Monthly.json")
   
   #### Total # of Video Views across LATAM Kids Channels ####
   print "Fetching SourceType wise Monthly data for LATAM Content Owner.."
   
   
   os.system("python yt_analytics_report.py --metrics=views,estimatedMinutesWatched --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=insightTrafficSourceType --feed=LATAM_SourceTypeDim_AllData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,estimatedMinutesWatched --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='uploaderType==self;claimedStatus==claimed' --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=insightTrafficSourceType --feed=LATAM_SourceTypeSelfClaimed_AllData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,estimatedMinutesWatched --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='uploaderType==thirdParty;claimedStatus==claimed' --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=insightTrafficSourceType --feed=LATAM_SourceTypeThirdPartyClaimed_AllData_Monthly.json")
   
   #### Total # of Video Views across LATAM Kids Channels ####
   print "Fetching DeviceType wise Monthly data for LATAM Content Owner.."
   
   
   os.system("python yt_analytics_report.py --metrics=views,estimatedMinutesWatched --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=deviceType --feed=LATAM_DeviceTypeDim_AllData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,estimatedMinutesWatched --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='uploaderType==self;claimedStatus==claimed' --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=deviceType --feed=LATAM_DeviceTypeSelfClaimed_AllData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=views,estimatedMinutesWatched --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --filters='uploaderType==thirdParty;claimedStatus==claimed' --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=deviceType --feed=LATAM_DeviceTypeThirdPartyClaimed_AllData_Monthly.json")
   
   
   print "Fetching Top 10 videos for LATAM Content Owner.."
   
   os.system("python yt_analytics_report.py --metrics=estimatedMinutesWatched,averageViewDuration,averageViewPercentage,views,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --max-results=10 --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=video --sort=-estimatedMinutesWatched --feed=LATAM_Top10Videos_AllData_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=estimatedMinutesWatched,averageViewDuration,averageViewPercentage,views,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --max-results=10 --filters='uploaderType==self;claimedStatus==claimed' --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=video --sort=-estimatedMinutesWatched --feed=LATAM_Top10VideosClaimedSelf_Monthly.json")
   
   os.system("python yt_analytics_report.py --metrics=estimatedMinutesWatched,averageViewDuration,averageViewPercentage,views,subscribersGained,subscribersLost --content-owner=8QEwoNWfiwUx3pS6OC0ArQ --max-results=10 --filters='uploaderType==thirdParty;claimedStatus==claimed' --start-date=2017-11-01 --end-date=2017-11-30 --dimensions=video --sort=-estimatedMinutesWatched --feed=LATAM_Top10VideosClaimedThirdParty_Monthly.json")
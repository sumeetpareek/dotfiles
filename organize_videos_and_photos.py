import os
import re
import glob
import datetime


# Configure full source and destination paths with trailing slash
source_directory = '/Users/sumeetpareek/Movies/source_dump/'
destination_directory = '/Users/sumeetpareek/Movies/organized_destination/'

# If the source has mp4 video files, iterate on them and print their year, month and date
for full_video_path in glob.glob(source_directory + 'VID*mp4'):
    video_filename = os.path.basename(full_video_path)
    match = re.match("VID_([0-9]{8})_", video_filename)
    
    if (match):
        date_time_obj = datetime.datetime.strptime(match.group(1), '%Y%m%d')
        year_of_video = date_time_obj.strftime('%Y')
        month_of_video = date_time_obj.strftime('%m') + '-' + date_time_obj.strftime('%B')
        day_of_video = date_time_obj.strftime('%d') + '-' + date_time_obj.strftime('%A')
        
        if not os.path.isdir(destination_directory + year_of_video):
            os.mkdir(destination_directory + year_of_video)
        if not os.path.isdir(destination_directory + year_of_video + '/' + month_of_video):
            os.mkdir(destination_directory + year_of_video + '/' + month_of_video)
        if not os.path.isdir(destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video):
            os.mkdir(destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video)
        
        os.rename(full_video_path, destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video + '/' + video_filename)

        

# date_time_str = 'Jun 28 2018  7:40AM'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')

# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)
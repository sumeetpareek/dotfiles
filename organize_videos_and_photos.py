import os
import re
import glob
from datetime import datetime
import errno

# Configure full source and destination paths with trailing slash
source_directory = '/Users/sumeetpareek/Movies/greece-honeymoon/dump_of_iphoneSE/'
destination_directory = '/Users/sumeetpareek/Movies/greece-honeymoon/organized_photos/'

capture_device = "iphoneSE"

# If the source has mp4 video files, iterate on them and print their year, month and date
# Default video filename patterns by devices
# Android Pixel 3a = VID_20191013_113715.mp4
# iOS iPhone SE = IMG_9198.MOV
if capture_device is 'pixel3A':
    for full_video_path in glob.glob(source_directory + 'VID*mp4'):
        video_filename = os.path.basename(full_video_path)
        match = re.match("VID_([0-9]{8})_", video_filename)
        
        if (match):
            date_time_obj = datetime.strptime(match.group(1), '%Y%m%d')
            year_of_video = date_time_obj.strftime('%Y')
            month_of_video = date_time_obj.strftime('%m') + '-' + date_time_obj.strftime('%B')
            day_of_video = date_time_obj.strftime('%d') + '-' + date_time_obj.strftime('%A')
            
            if not os.path.isdir(destination_directory + year_of_video):
                os.mkdir(destination_directory + year_of_video)
            if not os.path.isdir(destination_directory + year_of_video + '/' + month_of_video):
                os.mkdir(destination_directory + year_of_video + '/' + month_of_video)
            if not os.path.isdir(destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video):
                os.mkdir(destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video)
            
            filename_parts = video_filename.split('_')
            subparts = filename_parts[2].split('.')
            newfilename = date_time_obj.strftime('%Y%m%d_%a_') + subparts[0] + '_pixel3A.mp4'
            newfullpath = destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video + '/' + newfilename
            os.rename(full_video_path, newfullpath)

if capture_device is 'iphoneSE':
    for full_video_path in glob.glob(source_directory + 'IMG_*PNG'):
        video_filename = os.path.basename(full_video_path)
        video_modified_time = datetime.fromtimestamp(os.path.getmtime(full_video_path))
        year_of_video = video_modified_time.strftime('%Y')
        month_of_video = video_modified_time.strftime('%m') + '-' + video_modified_time.strftime('%B')
        day_of_video = video_modified_time.strftime('%d') + '-' + video_modified_time.strftime('%A')

        if not os.path.isdir(destination_directory + year_of_video):
            os.mkdir(destination_directory + year_of_video)
        if not os.path.isdir(destination_directory + year_of_video + '/' + month_of_video):
            os.mkdir(destination_directory + year_of_video + '/' + month_of_video)
        if not os.path.isdir(destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video):
            os.mkdir(destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video)

        newfilename = video_modified_time.strftime('%Y%m%d_%a_%H%M%S') + '_iphoneSE.PNG'
        newfullpath = destination_directory + year_of_video + '/' + month_of_video + '/' + day_of_video + '/' + newfilename
        os.rename(full_video_path, newfullpath)


# HOW TO CREATE AN EMPTY FILE
# ===========================       
# try:
#     os.close(os.open(newfullpath, os.O_CREAT|os.O_EXCL))
# except OSError as exc:
#     if exc.errno != errno.EEXIST:
#         raise   
        

# for full_video_path in glob.glob(source_directory + 'IMG*MOV'):

# date_time_str = 'Jun 28 2018  7:40AM'
# date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y %I:%M%p')

# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)
import os
import re
import glob
from datetime import datetime
import errno

# Configure full source and destination paths with trailing slash
sourceDirectory = '/Volumes/Sumeets WD 4TB/TODOsource/'
photos_destination_directory = '/Volumes/Sumeets WD 4TB/TODOorganizedphotos/'
videos_destination_directory = '/Volumes/Sumeets WD 4TB/TODOorganizedvideos/'
destination_directory = ''

flagCopy = False
flagMove = True

# Values you can use for filenameStyle:
# sequencial (eg: IMG_9083.JPG, IMG_8113.MOV, etc)
# dateandtime (eg: VID_20190925_191313.mp4, IMG_20190925_191313.jpg, PANO_20190925_191313.jpg, etc)
# dateandtimeextended (eg: IMG_20190812_183313994.jpg, etc)
filenameStyle = 'sequencial'
# Recommended values for itemLabel use the captureDevice and if necessary some other identifier
# eg: pixel3A, iphoneSE, lauraOppo, mummyLava, papaLava, etc.
itemLabel = 'iphoneSE'

# ==================================================================================================================================================================


# TODO function documentation

def organizeItem(itemFullPath, itemExtension, itemDateTimeObject, itemCaptureTimestamp):
    # Like 1947
    year_of_item = itemDateTimeObject.strftime('%Y')
    # Like 08-August
    month_of_item = itemDateTimeObject.strftime('%m') + '-' + itemDateTimeObject.strftime('%B')
    # Like 15-Friday
    day_of_item = itemDateTimeObject.strftime('%d') + '-' + itemDateTimeObject.strftime('%A')

    # Create organized nested folders like
    # `DESTINATION/1947/08-August/15-Friday`
    if not os.path.isdir(destination_directory + year_of_item):
        os.mkdir(destination_directory + year_of_item)
    if not os.path.isdir(destination_directory + year_of_item + '/' + month_of_item):
        os.mkdir(destination_directory + year_of_item + '/' + month_of_item)
    if not os.path.isdir(destination_directory + year_of_item + '/' + month_of_item + '/' + day_of_item):
        os.mkdir(destination_directory + year_of_item + '/' + month_of_item + '/' + day_of_item)
    
    # newFilename will be of the format: 
    # `itemDate_itemDay_itemTime_itemLabel.itemExtension`
    # eg: TODO
    newFilename = itemDateTimeObject.strftime('%Y%m%d_%a_') + itemCaptureTimestamp + '_' + itemLabel + '.' + itemExtension
    newFullPath = destination_directory + year_of_item + '/' + month_of_item + '/' + day_of_item + '/' + newFilename
    if flagMove and (not flagCopy):
        os.rename(itemFullPath, newFullPath)
        # When a dump is organized it is difficult to tell which months and dates the files got organized against.
        # This printing here is a rudimentary log that helps us know that.
        print 'file [[' + itemFilename +']] was moved to ' + newFullPath
    else:
        print "TODO the copy work should go here"


# ==================================================================================================================================================================


# If the source has mp4 video files, iterate on them and print their year, month and date
# Default video filename patterns by devices
# Android Pixel 3a = VID_20191013_113715.mp4
# iOS iPhone SE = IMG_9198.MOV
if filenameStyle is 'dateandtime':
    for itemFullPath in glob.glob(sourceDirectory + 'IMG*jpg'):
        itemExtension = 'jpg'
        destination_directory = photos_destination_directory
        
        itemFilename = os.path.basename(itemFullPath)
        match = re.match("IMG_([0-9]{8})_([0-9]{6}).jpg", itemFilename)
        
        if (match):
            itemDateTimeObject = datetime.strptime(match.group(1), '%Y%m%d')
            itemCaptureTimestamp = match.group(2)
            organizeItem(itemFullPath, itemExtension, itemDateTimeObject, itemCaptureTimestamp)

    for itemFullPath in glob.glob(sourceDirectory + 'VID*mp4'):
        itemExtension = 'mp4'
        destination_directory = videos_destination_directory
        
        itemFilename = os.path.basename(itemFullPath)
        match = re.match("VID_([0-9]{8})_([0-9]{6}).mp4", itemFilename)
        
        if (match):
            itemDateTimeObject = datetime.strptime(match.group(1), '%Y%m%d')
            itemCaptureTimestamp = match.group(2)
            organizeItem(itemFullPath, itemExtension, itemDateTimeObject, itemCaptureTimestamp)

if filenameStyle is 'sequencial':
    for itemFullPath in glob.glob(sourceDirectory + 'IMG*JPG'):
        itemExtension = 'jpg'
        destination_directory = photos_destination_directory
        
        itemFilename = os.path.basename(itemFullPath)
        match = re.match("IMG_([0-9]{1,5}).JPG", itemFilename)
        
        if (match):
            itemDateTimeObject = datetime.fromtimestamp(os.path.getmtime(itemFullPath))
            itemCaptureTimestamp = itemDateTimeObject.strftime('%H%M%S')
            organizeItem(itemFullPath, itemExtension, itemDateTimeObject, itemCaptureTimestamp)

    for itemFullPath in glob.glob(sourceDirectory + 'IMG*MOV'):
        itemExtension = 'MOV'
        destination_directory = videos_destination_directory
        
        itemFilename = os.path.basename(itemFullPath)
        match = re.match("IMG_([0-9]{1,5}).MOV", itemFilename)
        
        if (match):
            itemDateTimeObject = datetime.fromtimestamp(os.path.getmtime(itemFullPath))
            itemCaptureTimestamp = itemDateTimeObject.strftime('%H%M%S')
            organizeItem(itemFullPath, itemExtension, itemDateTimeObject, itemCaptureTimestamp)

if filenameStyle is 'dateandtimeextended':
    for itemFullPath in glob.glob(sourceDirectory + 'IMG*jpg'):
        itemExtension = 'jpg'
        destination_directory = photos_destination_directory
        
        itemFilename = os.path.basename(itemFullPath)
        match = re.match("IMG_([0-9]{8})_([0-9]{6})([0-9]{3}).jpg", itemFilename)
        
        if (match):
            itemDateTimeObject = datetime.strptime(match.group(1), '%Y%m%d')
            itemCaptureTimestamp = match.group(2)
            organizeItem(itemFullPath, itemExtension, itemDateTimeObject, itemCaptureTimestamp)

    for itemFullPath in glob.glob(sourceDirectory + 'VID*mp4'):
        itemExtension = 'mp4'
        destination_directory = videos_destination_directory
        
        itemFilename = os.path.basename(itemFullPath)
        match = re.match("VID_([0-9]{8})_([0-9]{6})([0-9]{3}).mp4", itemFilename)
        
        if (match):
            itemDateTimeObject = datetime.strptime(match.group(1), '%Y%m%d')
            itemCaptureTimestamp = match.group(2)
            organizeItem(itemFullPath, itemExtension, itemDateTimeObject, itemCaptureTimestamp)


# HOW TO CREATE AN EMPTY FILE
# ===========================       
# try:
#     os.close(os.open(newfullpath, os.O_CREAT|os.O_EXCL))
# except OSError as exc:
#     if exc.errno != errno.EEXIST:
#         raise   


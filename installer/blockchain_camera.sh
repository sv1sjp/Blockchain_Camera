#!/bin/bash


#Read the number of the videos have ever recorded by BlockchainCam
name=$(cat ../logs/video_count)

# increase by one in order to name the new video that it will be captured
name=$((name+1))

#record for 10 minutes using ffmpeg- you have to edit manually and add your camera and microphone and edit the minutes it captures.
#For more information, read the docs
ffmpeg  -f video4linux2  -r 28 -i /dev/video0 -f alsa -ac 2 -i hw:1,0  -t 00:00:10 ../videos/blockchaincam_$name.mp4

#save the new sum of videos have ever recorded by BlockchainCam
echo $name > ../logs/video_count

# hash the video and save it as a file
sha512sum ../videos/blockchaincam_$name.mp4 | awk '{print $1}' > hashes

# send the hash to Ethereum Blockchain
python3 send_to_blockchain.py

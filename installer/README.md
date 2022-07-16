# Install Blockchain Camera software to any GNU/Linux device.
___
For more information about how it works and how you can create your own Blockchain Camera and implementation idead, reading the full paper is recommended. Click here

## Video Presentations
YouTube: 

Presentation of Blockchain Camera in English 

Presentation of Blockchain Camera in Greek

LBRY: 

Presentation of Blockchain Camera in English 

Presentation of Blockchain Camera in Greek
___
Blockchain Camera software provides an automated installation script which will create and configure all the files are necessary in order to have a full functional Blockchain Camera. At first, we have to download the entire installer folder from Github and then run the setup.py. Then, the installer will ask about the BlockchainCamera’s Smart-Contract address, the private key of the wallet, and the http link from the node that it will be used to interact with Blockchain.
On my own example, I used the infrastructure from Infura.  Infura provides a Blockchain node infrastructure service that allows apps and developers to get data from, and broadcast transactions to the Ethereum Blockchain. Infura provides access to the Mainnet as well as to the test Networks. For example, I connected my own Blockchain Camera to Ropsten Testnet Ethereum Network, in which I deployed the Blockchain Camera Smart-Contract too.
When we add the private key from the wallet we deployed the Blockchain Camera Smart-Contract, system will automatically will hash the lsusb and then encrypt the data as key with aes256-cbc encryption cipher of the lsusb the devices that are connected to Blockchain Camera. It is mandatory to remove all the devices that they will not be connected on the camera when the installer will ask us to enter the private key.

The installer will make our system ready to record videos and then send the hashes to Blockchain. 

Blockchain Camera files are divided into 3 subfolders:
- logs: where the log files are stored.
- src: where the Blockchain Camera applications are stored.
- videos: where the videos are stored.
Moreover, installer will produce 2 Validation Tools, one CLI version and one GUI version, which can connect and read data only from the Smart-Contract address the administrator has entered before, due to installation process. If user wants to connect it to a different Blockchain Camera, it is recommended to run the installer again and then enter as an input only the smart-contract address he wants to be able to connect.

In blockcain_camera.sh, device administrator must configure ffmpeg to record from its own camera or/and microphone and choose the minutes he wants to record before hashing the video. The Python software send_to_blockchain.py is called from blockcain_camera.sh or retry.py in order to send a hash to Blockchain. 
For example, Raspberry Pi  ffmpeg configuration for only video recording with audio for 10 minutes is:

```
ffmpeg  -f video4linux2  -r 28 -i /dev/video0 -f alsa -ac 2 -i hw:1,0  -t 00:10:00 ../videos/blockchaincam_$name.mp4
```

Furthermore, to activate the Blockchain Camera to run every 10minutes we have to create a cronjob to force it re-run. On the next subchapter we will discuss about how cron works and how to use it.
Retry.py is an optional script that can be used in order to check from the log files if a hash failed to be sent to Blockchain and if not, it will call send_to_blockchain.py to send it again. To activate it, it is recommended to create a cronjob to check for failures every 7-15 minutes. 

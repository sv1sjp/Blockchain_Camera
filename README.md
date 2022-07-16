# Blockchain_Camera

Turn your Raspberry Pi into an Ethereum-based Blockchain Camera! Powered by Solidity and Python.



Blockchain Camera provides an easy and safe way to capture and guarantee the existence of videos reducing the impact of modified videos as it can preserve the integrity and validity of videos using Blockchain Technology. Blockchain Camera sends to Ethereum Network the hash of each video and the time the video has been recorded in order to be able validate that a video is genuine and hasn't been modified using a Blockchain Camera Validation Tool.

In folder "installer" an installation tutorial can be found. 

For more information about how it works and how you can create your own Blockchain Camera and implementation idead, reading the full paper is recommended. 
Click here



## Video Presentations

YouTube:
Presentation of Blockchain Camera in English
Presentation of Blockchain Camera in Greek

LBRY:
Presentation of Blockchain Camera in English
Presentation of Blockchain Camera in Greek

_____

# Blockchain Camera Validator Tools User Manual:
## Depedencies

Blockchain Camera Validator Tools in order to be functional need Python3 to be installed with the library of web3. Web3 can be installed very easily with the command:
```
pip install web3
```

Moreover, Blockchain Camera GUI needs PySimpleGUI library too. PySimpleGUI can be installed very easily with the command:
```
pip install PySimpleGUI
```
## Hashing a Video
As has already mentioned before, Blockchain Camera hashes are created by using a
SHA-512 hash function and then stored to Blockchain. As users, when we want to validate that a video is genuine, at first we have to download the video from a centralized center with the events that we want to validate if they really happened. 
We can hash a video by using sha512sum tool from GNU/Linux or other Unix like Operating Systems by typing:
```
sha512sum $NAME_OF_FILE.mp4
```
sha512sum tool will return a hash we can copy and then paste to a Blockchain Camera Validator Tool (GUI or CLI) in order to check if that hash really exists in Blockchain.
Blockchain Camera Validator Tool GUI is recommended to be used from normal users as it offers a nice-looking interface where users can interact with Blockchain Camera Smart-Contract very easily. However, in order to be functional, keep in mind that the script must be edited and a node must be added by user. Without a node, Blockchain Camera Validator Tool cannot interact with Blockchain. If you do not want to create your own Ethereum Node you can use a company’s node infrastructure, for example from Infura, and then paste the appropriate HTTPProvider link to w3 variable.

Furthermore, user can very easily copy the video’s hash from the sha512sum command and paste it to Blockchain Camera Validator GUI and then press Enter. Blockchain Camera will download a full copy of the Blockchain Camera Smart-Contract’s and using basic Python function it will find out if the hash exists in the list. If the hash exists, the tool will return the message:
“The hash exists in the list. That means the video is genuine and its hash has been mined to Blockchain at: <UNIX_TIME_CONVERTED_TO_LOCAL>“ and then it will show the time the hash has been sent to Blockchain. 

If the video’s hash has not been sent to Blockchain, The Blockchain Validator Tool returns a message of “This hash is not genuine.”.
 ## Command Line version of Blockchain Camera Validation Tool
Blockchain Camera Validator CLI is the backend version of the GUI version of the app. Blockchain Camera Validator Tool CLI comes as an easier command line-based tool in order to be implemented to other projects and extend its futures much easier. As the GUI version for being functional, user must add a node to the program. Blockchain Camera Validator Tool CLI works exact the same as the GUI. All the user has to do is to paste a hash as an input and the application will return if the hash exists to Blockchain Camera Smart-Contract. However, CLI mode has some special futures which are missing from GUI version.
For Example, Blockchain Camera Validator Tool CLI supports multi hash validation. All we have to do is to create a new file at the same file with the Blockchain Camera Validator Tool CLI and paste one hash on each line. Then, we run the tool and we choose multiple and then we enter as an input the name of the file. File’s location must be on the same folder with the Blockchain Camera Validator CLI Application. Blockchain Camera Validator tool will check each hash if exists in the Blockchain or not and it will return the result.


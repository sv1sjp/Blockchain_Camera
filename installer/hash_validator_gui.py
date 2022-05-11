"""
Copyright (C) 2022  Dimitris Vagiakakos (sv1sjp)
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or any later version. This program 
is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this document. 
 If not, see https://www.gnu.org/licenses/gpl-3.0.html
For any information, find me on: https://sv1sjp.github.io 
or contact me at: dimitrislinuxos@protonmail.ch or @sv1sjp in any social media platform.

"""


from web3 import Web3
from web3.auto import w3
import PySimpleGUI as sg
import json,datetime

print("	Blockchain Camera Validator GUI - created by DimitrisV SV1SJP.")
print('''                                                                          
      @&&&&&&&&&&&&&&&                                                   *&,    
    &&&&&&&&&&&&&&&,                                                        @   
   .&&&&&&/*%&&&&&&                                                         .&  
   .&&&&%/////&&&&&                    ,**,    ..   ,***.                   .&  
   .&&&&&&@&&&&&&&&                 ,, .///////////////, ,**                .&  
   .&&&&@****&&&&&&              ., .//////////,./////////* **              .&  
   .&&&&@****#&&&&&             ,. ///////////  ..*/////////, *,            .&  
   .&&&&&&&&&&&&&&&            ,..//////////    ..../////////* *,           .&  
   .&&&&&&&&&&&&&&&           ,. //////////    .*....*////////..,           .&  
   .&&&&&&&&&&&&&&&           ...//////// ......******,///////* ,.          .&  
   .&&&&&&&&&&&&&&&           .. /////////.//...****/,*///////. ,           .&  
   .&&&&&&&&&&&&&&&            . ,/////////,   */,..,///////// ,,           .&  
   .&&&&&&&&&&&&&&&             . .//////////.  ...////////// ,,            .&  
   .&&&@@&@@@&@@&&&              .. *////////// .//////////  ..             .&  
   .&&&&@(&@%(@&&&&                ..  /////////////////. ...               .&  
   .&&&@@#(@(#@@&&&                   ...   .,*/**,   ....                  .&  
   .&&&@&@#(%@&@&&&                         ........                        .&  
    @&&&&@%(%@&&&&&                                                         @/  
     (&&&&&&&&&&&&&&@                                                     #@    
         .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,      
	 ''')

try:
	# connect to the node
	w3 = Web3(Web3.HTTPProvider('<ΙNSERT_YOUR_NODE_HERE>'))

	#adresses
	contract_address="<ΙNSERT_YOUR_CONTRACT_ADDRESS_HERE>"

	#smart_contract abi
	contract_abi= [
		{
			"inputs": [
				{
					"internalType": "string",
					"name": "_hash",
					"type": "string"
				}
			],
			"name": "addHash",
			"outputs": [],
			"stateMutability": "nonpayable",
			"type": "function"
		},
		{
			"inputs": [],
			"stateMutability": "nonpayable",
			"type": "constructor"
		},
		{
			"inputs": [],
			"name": "owner",
			"outputs": [
				{
					"internalType": "address payable",
					"name": "",
					"type": "address"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [],
			"name": "viewHashes",
			"outputs": [
				{
					"internalType": "string[]",
					"name": "hash",
					"type": "string[]"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [],
			"name": "viewIndex",
			"outputs": [
				{
					"internalType": "uint256",
					"name": "_index",
					"type": "uint256"
				}
			],
			"stateMutability": "view",
			"type": "function"
		},
		{
			"inputs": [],
			"name": "viewTimeStamps",
			"outputs": [
				{
					"internalType": "uint256[]",
					"name": "_time_of_hash",
					"type": "uint256[]"
				}
			],
			"stateMutability": "view",
			"type": "function"
		}
	]





	#Connect to smart contract
	blockchaincamera_contract = w3.eth.contract(address=contract_address, abi=contract_abi)

	#Retrieve from Blockchain all the hashes and datetimes in unix format
	AllHashes = blockchaincamera_contract.functions.viewHashes().call()
	AllTime = blockchaincamera_contract.functions.viewTimeStamps().call()
	

	#Apply the GUI theme
	sg.theme('Dark Blue 6')

	# Define the window's contents
	layout = [[sg.Text("Blockchain Camera Validator Check.\n Enter a hash:",size=(50,2), font=("Helvetica", 15), justification='center')], 
			[sg.Input(key='-INPUT-' , justification='center')],
			[sg.Button('Enter',size=(30,1)), sg.Button('Exit',size=(20,1)) , sg.Button('About',size=(8,1))  ]], [sg.Text(size=(100,4),  key='-OUTPUT-', font=("Helvetica", 11) , justification='center')]

	# Create the window
	window = sg.Window('Blockchain Camera Validator', layout,icon='blockchain_camera.ico', element_justification='c',size=(500, 170),grab_anywhere=True)
	

	# Display and interact with the Window using an Event Loop
	while True:
		event, values = window.read()
		# See if user wants to quit or window was closed
		if event == sg.WINDOW_CLOSED or event in ('Exit', None):
			break
		# input from the hash
		hash= str(values['-INPUT-'])

		#search for the hash when enter is pressed
		if event in ('Enter', None):
			
			if hash in AllHashes:
				index= AllHashes.index(hash)
				window['-OUTPUT-'].update("The hash exists in the list. \nThat means the video is genuine and its hash has been mined to Blockchain at: \n " + (datetime.datetime.fromtimestamp(int(AllTime[index])).strftime('%d-%m-%Y %H:%M:%S')))
			else:
				window['-OUTPUT-'].update("This video is not genuine.")
		if event in ("About", None):
			window_about=sg.Window("About", [[sg.Text("Blockchain Camera is created by DimitrisV SV1SJP under GNU GPL v3.0  \n\n Find more awesome projects: https://sv1sjp.github.io\n \n Buy me a coffee:  0x3f27F05Ca28a5B5F876A3A7d435E2E852756F873", size=(70,5), font=("Helvetica", 15), justification='center')],[ sg.Button('Close', size=(100,1))]  ])
			
			while True:
				event1,values1= window_about.read()
				if event1 == sg.WINDOW_CLOSED or event1 in ('Close',None):
					window_about.close()
					break
			


		# input from the hash
		hash= str(values['-INPUT-'])


except:  
    window['-OUTPUT-'].update("An Error occured, try again later!")
    

    
    


# Finishing up by removing from the screen
window.close()    
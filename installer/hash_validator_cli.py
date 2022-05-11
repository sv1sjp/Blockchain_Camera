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
import json,datetime

def hashcheck(hash):
	print("______________________________________________")
	print("Hash: "+hash)
	if hash in AllHashes:
		index= AllHashes.index(hash)
		print("\nThe hash exists in the list. \nThat means the video is genuine and its hash has been mined to Blockchain at: \n")
		print(datetime.datetime.fromtimestamp(int(AllTime[index])).strftime('%d-%m-%Y %H:%M:%S'))
	else:
		print("\nThis hash is not genuine.")
	print("______________________________________________")
try:
	w3 = Web3(Web3.HTTPProvider('<ΙNSERT_YOUR_NODE_HERE>'))

	#adress
	contract_address="<ΙNSERT_YOUR_CONTRACT_ADDRESS_HERE>"

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
	print("		Blockchain Camera Validator GUI - created by DimitrisV SV1SJP.")
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
	
	#Check the input
	question= input(" Do you want to check a single file or multiple hashes from a file? (single/multiple): ")
	while True:
		if question=="single" or question=="multiple":
			break
		else:
			question= input("Wrong arguments. Do you want to check a single file or multiple hashes from a file? (single/multiple): ")
	#Check only one hash
	if question=="single":
		hash=input("\n Enter a hash: ")
		hashcheck(hash)
	else:
		try:
			#Check multiple hashes from a file.
			f=input("Give the name of the file. \n Note: The file must have one hash by line and be located in the same folder with this software\n Enter the file name: ")
			file= open(f,"r")

			for line in file:
				hashcheck(line.strip())
		except: 
			print("This file does not exists.")
		
	
except:
    print("An Error occured, try again later!")  



	
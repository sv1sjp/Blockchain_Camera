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
import readline
from web3 import Web3
from web3.auto import w3
import json,os,logging,subprocess,base64





hash="0"
logging.basicConfig(format='%(asctime)s - %(message)s', filename="../logs/blockchaincamera.log", level=logging.INFO)
try:
	
	# connect to the node
	w3 = Web3(Web3.HTTPProvider('<ΙNSERT_YOUR_NODE_HERE>'))

	#adresses
	contract_address="<ΙNSERT_YOUR_CONTRACT_ADDRESS_HERE>"  
	wallet_address='<ΙNSERT_YOUR_WALLET_ADDRESS_HERE>'

	#file with new hashes
	if os.path.exists("hashes"):
		file= open("hashes","r")
		hash=file.readline().strip()
	
		

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

		
		blockchaincamera_contract = w3.eth.contract(address=contract_address, abi=contract_abi)
		nonce = w3.eth.getTransactionCount(wallet_address) 

		

	# Decrypt the wallet's private key. 
		# Note if you disconnected any storage device from the BlockchainCamera
		# the key would have been destroyed. Run the installer again and re-add your private key.

		transaction= blockchaincamera_contract.functions.addHash(hash).buildTransaction({
			'chainId': 3,
			'gas': 4600000,
			'from': wallet_address,
			'nonce': nonce
			}) 
		#Note if you don't want to use encryption, just replace line 132 with the line 131
		#signed_txn = w3.eth.account.signTransaction(transaction,'ΙNSERT_YOUR_PRIVATE_KEY_HERE>')
		signed_txn = w3.eth.account.signTransaction(transaction,str(subprocess.check_output('echo "<ΙNSERT_YOUR_PRIVATE_AES_ENCRYPTED_KEY_HERE>" | openssl enc -aes-256-cbc -d -a -md sha256 -pbkdf2 -pass pass:$(lsusb | sha256sum)', shell=True))[2:66])
		tx_hash= w3.eth.send_raw_transaction(signed_txn.rawTransaction)
		
		

		logging.info("Hash " + hash + " has been added successfully. ")
		os.remove("hashes")
	else: 
		logging.error("There is no hash file. Nothing has been sent to Blockchain.") 	
except:
	logging.error("Problem with the connection. Hash " + hash + " hasn't been sent to Blockchain.") 

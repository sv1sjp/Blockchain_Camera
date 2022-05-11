// SPDX-License-Identifier: GPL-3.0+
pragma solidity 0.8.13;


contract BlockchainCamera {


    // Creating a mapping
    string[] private hashes;
    address payable public  owner;
    uint private index=0;
    uint[] private time_of_hash;


    constructor()  {
        owner = payable(msg.sender);
        hashes.push("start");
        index = index + 1;
        time_of_hash.push(block.timestamp);

  } 

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    function addHash(string memory _hash) public onlyOwner {
        
        hashes.push(_hash);
        time_of_hash.push(block.timestamp);
        index= index +1;
        
    }

    function viewHashes() public view returns (string[] memory hash) {
        return hashes;
    }

    function viewIndex() public view returns (uint _index)
    {
        return index;
    }

    function viewTimeStamps() public view returns (uint[] memory _time_of_hash) {
        return time_of_hash;
    }
    

}

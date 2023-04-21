# Encrypted-Data-Storage-for-Access-Control-in-Blockchain
The project is the extension of master's dissertation that aims to provide proof of concept.

The Aim is to provide access control in blockchain environment. Preserves Confidentiality by encrypting data using public key, uses advantage of blockchain to maintain Integrity and Availability.

RSA 1024 is used to generate key pair of public and private key when user signup for the first time, public key is uploaded to database of an ORG, and private key is given to user it self. 

The Flask app then allows user to select public key of the receipient (taken from database) and encrypts the data (data can be anything , it will can be coverted to hex values) and then can be uploaded on the blockchain. only the intended recepient will be able see the data on thier flask app. using blockchain negets the possibilty of repudiation.

Please note this is just a proof of concept and may introduce vulneribility in code. The blockchain of choice for this project was Multichain.

The Future work will include direct integration with any blockchain which uses json-rpc , improved public key exchange, and full network configuration guide to successfully and securly implement in an ORG. 

Contact for more information.





https://user-images.githubusercontent.com/53125151/233697291-13f7156b-df2a-4a2a-b9b5-31d51c4cdb88.mp4


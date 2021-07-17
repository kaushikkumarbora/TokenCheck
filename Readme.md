## TokenCheck: Towards Deep Learning Based Security Vulnerability Detection In ERC-20 Tokens
The use of Ethereum based tokens in blockchain applications have been on the rise in recent times and accordingly, the need for proper analysis of token source codes for security vulnerabilities has become paramount. Existing symbolic analysis tools have demonstrated to be efficient in detecting many of the security vulnerabilities, but by virtue of the complex nature of the analysis they perform to detect vulnerable paths, there is a considerable increase in search time with an increase in depth. Cryptocurrencies have recently achieved the milestone of a USD 2 trillion market cap and with such a high volume of assets involved, the need for an efficient and scalable security vulnerability detection tool in an ever-increasing list of tokens becomes of utmost priority. This paper proposes a deep learning based approach for the prediction of security vulnerabilities in ERC-20 token smart contracts. The proposal proposed by this paper is based on the use of Long Short-Term Memory neural network architecture on smart contract opcodes which are in form of sequential data. The proposed solution achieves an accuracy of 93.26% when tested on ERC-20 smart contracts collected from Ethereum mainnet and thus proves to be an efficient alternative for existing symbolic tools

### Steps to run the application

1. `cd saved model`
   
2. `pip install -r requirements.txt` (only for the first time) then `python saved.py`

3. Check for smart contract bytecodes.

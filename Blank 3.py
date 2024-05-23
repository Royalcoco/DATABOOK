blockchain_project/
│
├── blockchain/
│   ├── __init__.py
│   ├── blockchain.py
│   ├── block.py
│   └── nft.py
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── database.py
│
├── main.py
├── requirements.txt
└── README.md
from .blockchain import Blockchain
from .nft import NFT

blockchain = Blockchain()
nft = NFT()
import hashlib
import json
from time import time

class Block:
    def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.proof = proof
        self.timestamp = timestamp or time()
    
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
import json
from .block import Block
from time import time
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", [], 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def create_block(self, proof, previous_hash):
        block = Block(len(self.chain), previous_hash, self.pending_transactions, proof)
        block.hash = block.compute_hash()
        self.chain.append(block)
        self.pending_transactions = []
        return block

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def add_transaction(self, sender, receiver, amount):
        self.pending_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.get_last_block().index + 1

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block.previous_hash != previous_block.compute_hash():
                return False
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
class NFT:
    def __init__(self):
        self.ledger = {}

    def mint_nft(self, owner, metadata):
        nft_id = len(self.ledger) + 1
        self.ledger[nft_id] = {
            'owner': owner,
            'metadata': metadata
        }
        return nft_id

    def transfer_nft(self, nft_id, new_owner):
        if nft_id in self.ledger:
            self.ledger[nft_id]['owner'] = new_owner
            return True
        return False

    def get_nft(self, nft_id):
        return self.ledger.get(nft_id, None)
from flask import Flask, jsonify, request
from .blockchain import blockchain, nft
from flask import Flask
from .routes import init_routes

def create_app(blockchain, nft):
    app = Flask(__name__)
    init_routes(app, blockchain, nft)
    return app
from flask import request, jsonify
from .database import db

def init_routes(app, blockchain, nft):
    
    @app.route('/mine', methods=['GET'])
    def mine_block():
        previous_block = blockchain.get_last_block()
        previous_proof = previous_block.proof
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = previous_block.compute_hash()
        block = blockchain.create_block(proof, previous_hash)
        nft_id = nft.mint_nft("miner_address", {"block_index": block.index})
        response = {
            'message': 'Congratulations, you just mined a block!',
            'index': block.index,
            'proof': block.proof,
            'previous_hash': block.previous_hash,
            'nft_id': nft_id
        }
        return jsonify(response), 200

    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        values = request.get_json()
        required = ['sender', 'receiver', 'amount']
        if not all(k in values for k in required):
            return 'Missing values', 400
        index = blockchain.add_transaction(values['sender'], values['receiver'], values['amount'])
        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201

    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': [block.__dict__ for block in blockchain.chain],
            'length': len(blockchain.chain)
        }
        return jsonify(response), 200

    @app.route('/nft/<int:nft_id>', methods=['GET'])
    def get_nft(nft_id):
        nft_data = nft.get_nft(nft_id)
        if nft_data:
            return jsonify(nft_data), 200
        return jsonify({'message': 'NFT not found'}), 404
from app import create_app
from blockchain import blockchain, nft

app = create_app(blockchain, nft)

if __name__ == '__main__':
    app.run(debug=True)
Flask==2.0.2
# Blockchain Project

This project is a basic implementation of a blockchain with NFT rewards for mining.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Running the Application

1. Start the Flask server:
    ```
    python main.py
    ```
2. Access the endpoints to interact with the blockchain.

## Endpoints

- `/mine` : Mines a new block and mints an NFT as a reward.
- `/transactions/new` : Adds a new transaction.
- `/chain` : Returns the full blockchain.
- `/nft/<nft_id>` : Retrieves the details of a specific NFT.

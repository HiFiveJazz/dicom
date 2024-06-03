import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, current_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.current_hash = current_hash

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = self.create_block(data="Genesis Block", previous_hash="0")
        self.chain.append(genesis_block)

    def create_block(self, data, previous_hash):
        index = len(self.chain)
        timestamp = datetime.now().isoformat()
        block_string = json.dumps({
            'index': index,
            'previous_hash': previous_hash,
            'timestamp': timestamp,
            'data': data
        }, sort_keys=True).encode()
        current_hash = hashlib.sha256(block_string).hexdigest()
        return Block(index, previous_hash, timestamp, data, current_hash)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = self.create_block(data, previous_block.current_hash)
        self.chain.append(new_block)

    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.previous_hash != previous_block.current_hash:
                return False
            block_string = json.dumps({
                'index': current_block.index,
                'previous_hash': current_block.previous_hash,
                'timestamp': current_block.timestamp,
                'data': current_block.data
            }, sort_keys=True).encode()
            current_hash = hashlib.sha256(block_string).hexdigest()
            if current_block.current_hash != current_hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.current_hash}")
            print("\n")

    def get_ledger(self):
        ledger = []
        for block in self.chain:
            ledger.append({
                'index': block.index,
                'previous_hash': block.previous_hash,
                'timestamp': block.timestamp,
                'data': block.data,
                'hash': block.current_hash
            })
        return ledger

if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("First message")
    blockchain.add_block("Second message")
    blockchain.add_block("Third message")

    blockchain.display_chain()
    print(f"Is chain valid? {blockchain.verify_chain()}")
    print(json.dumps(blockchain.get_ledger(), indent=4))


import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce, current_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.current_hash = current_hash

    def to_dict(self):
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp,
            'data': self.data,
            'nonce': self.nonce
        }

    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, data, nonce):
        block_string = json.dumps({
            'index': index,
            'previous_hash': previous_hash,
            'timestamp': timestamp,
            'data': data,
            'nonce': nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = self.create_block(data="Genesis Block", previous_hash="0")
        self.chain.append(genesis_block)

    def create_block(self, data, previous_hash):
        index = len(self.chain)
        timestamp = datetime.now().isoformat()
        nonce, current_hash = self.proof_of_work(index, previous_hash, timestamp, data)
        return Block(index, previous_hash, timestamp, data, nonce, current_hash)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = self.create_block(data, previous_block.current_hash)
        self.chain.append(new_block)

    def proof_of_work(self, index, previous_hash, timestamp, data):
        nonce = 0
        while True:
            current_hash = Block.calculate_hash(index, previous_hash, timestamp, data, nonce)
            if current_hash[:self.difficulty] == '0' * self.difficulty:
                return nonce, current_hash
            nonce += 1

    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.current_hash:
                return False

            recalculated_hash = Block.calculate_hash(
                current_block.index,
                current_block.previous_hash,
                current_block.timestamp,
                current_block.data,
                current_block.nonce
            )

            if current_block.current_hash != recalculated_hash:
                return False

        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Nonce: {block.nonce}")
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
                'nonce': block.nonce,
                'hash': block.current_hash
            })
        return ledger

if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)
    blockchain.add_block("First message")
    blockchain.add_block("Second message")
    blockchain.add_block("Third message")

    blockchain.display_chain()
    print(f"Is chain valid? {blockchain.verify_chain()}")
    print(json.dumps(blockchain.get_ledger(), indent=4))


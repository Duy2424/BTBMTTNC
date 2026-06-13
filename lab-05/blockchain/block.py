# Dinh nghia mot khoi (Block) trong blockchain
import hashlib
import json
import time


class Block:
    def __init__(self, index, transactions, previous_hash, proof):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.compute_hash()

    def compute_hash(self):
        # Tinh gia tri hash SHA-256 cho noi dung cua khoi
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "proof": self.proof,
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

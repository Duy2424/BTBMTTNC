# Dinh nghia chuoi khoi (Blockchain)
import hashlib
from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        # Tao khoi dau tien (genesis block)
        self.create_genesis_block()

    def create_genesis_block(self):
        # Khoi genesis: index = 1, khong co giao dich, previous_hash = '0', proof = 1
        genesis_block = Block(1, [], "0", 1)
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        # Them mot giao dich vao danh sach cho xu ly
        self.pending_transactions.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
        })

    def proof_of_work(self, last_proof):
        # Tim proof sao cho valid_proof tra ve True
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        # Kiem tra proof: hash cua (last_proof + proof) bat dau bang '00'
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:2] == "00"

    def add_block(self, proof):
        # Tao khoi moi tu cac giao dich dang cho va them vao chuoi
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.pending_transactions,
            previous_hash=last_block.hash,
            proof=proof,
        )
        self.pending_transactions = []
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        # Kiem tra tinh hop le cua toan bo chuoi
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Kiem tra hash cua khoi hien tai
            if current.hash != current.compute_hash():
                return False

            # Kiem tra lien ket previous_hash
            if current.previous_hash != previous.hash:
                return False

        return True

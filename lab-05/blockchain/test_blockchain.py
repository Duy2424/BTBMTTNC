# Chuong trinh kiem tra blockchain
from blockchain import Blockchain


def print_block(block):
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Proof: {block.proof}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 50)


if __name__ == "__main__":
    # Tao blockchain moi
    blockchain = Blockchain()

    # Them cac giao dich
    blockchain.add_transaction("Alice", "Bob", 10)
    blockchain.add_transaction("Bob", "Charlie", 5)
    blockchain.add_transaction("Charlie", "Alice", 3)
    blockchain.add_transaction("Genesis", "Miner", 1)

    # Dao khoi moi (proof of work)
    last_proof = blockchain.get_last_block().proof
    proof = blockchain.proof_of_work(last_proof)
    blockchain.add_block(proof)

    # In thong tin cac khoi
    print("Block #1:")
    print_block(blockchain.chain[0])
    print("Block #2:")
    print_block(blockchain.chain[1])

    # Kiem tra tinh hop le cua chuoi
    print("Is Blockchain Valid:", blockchain.is_chain_valid())

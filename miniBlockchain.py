import hashlib
import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_str = str(self.index) + self.timestamp + self.data + self.previous_hash
        return hashlib.sha256(block_str.encode()).hexdigest()

    def display(self):
        print(f"Block {self.index} | {self.timestamp}")
        print(f"Data        : {self.data}")
        print(f"Prev Hash   : {self.previous_hash[:10]}....")
        print(f"Hash        : {self.hash[:10]}....\n")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last_block = self.get_last_block()
        new_block = Block(len(self.chain), data, last_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            cur = self.chain[i]
            prev = self.chain[i - 1]
            if cur.hash != cur.compute_hash():
                print(f"Tampered hash at block {i}")
                return False
            if cur.previous_hash != prev.hash:
                print(f"Hash link broken at block {i}")
                return False
        print("Blockchain is valid.")
        return True

# Usage
bc = Blockchain()
bc.add_block("Alice sends 1 BTC to Bob")
bc.add_block("Bob buys Coffee")

for block in bc.chain:
    block.display()

bc.is_chain_valid()

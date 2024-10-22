import hashlib
import time
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Blockchain base
Base = declarative_base()

# Bloc structure
class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

# Blockchain class
class Blockchain:
    def __init__(self, difficulty):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# SQLAlchemy Model to store blockchain in SQL
class SQLBlock(Base):
    __tablename__ = 'blocks'
    id = Column(Integer, Sequence('block_id_seq'), primary_key=True)
    index = Column(Integer)
    previous_hash = Column(String(64))
    timestamp = Column(String(64))
    data = Column(String)
    hash = Column(String(64))

# Setting up the SQL connection
def setup_database():
    engine = create_engine('sqlite:///blockchain.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def save_block_to_db(session, block):
    sql_block = SQLBlock(index=block.index, previous_hash=block.previous_hash,
                         timestamp=str(block.timestamp), data=block.data, hash=block.hash)
    session.add(sql_block)
    session.commit()

# Example usage
if __name__ == "__main__":
    # Setup blockchain and SQL
    blockchain = Blockchain(difficulty=4)
    session = setup_database()

    # Adding a few blocks with tasks (requests)
    blockchain.add_block(Block(1, blockchain.get_latest_block().hash, time.time(), "Task 1: Process image set A"))
    blockchain.add_block(Block(2, blockchain.get_latest_block().hash, time.time(), "Task 2: Process image set B"))

    # Save blocks to database
    for block in blockchain.chain:
        save_block_to_db(session, block)

    # Display the blockchain
    for block in blockchain.chain:
        print(f"Block {block.index} [Hash: {block.hash}] with data: {block.data}")

    # Query the database for blocks to process and process them in the database again with the correct hash
    blocks = session.query(SQLBlock).all()
    for block in blocks:
        print(f"Block {block.index} [Hash: {block.hash}] with data: {block.data}")
        
    # Close the session
    session.close()
    
    # Done with the blockchain
    
    # To delete the database, you can use the following code:
    # import os
    # os.remove("blockchain.db")
    
    # Done with the blockchain
    
    # To delete the database, you can use the following code:
    
    # import os
    # os.remove("blockchain.db")
    
    # Done with the blockchain
    
    # To delete the database, you can use the following code:
    
    # import os
    # os.remove("blockchain.db")
    
    # Done
    
    # To delete the database, you can use the following code:
    
    # import os
    
    # os.remove("blockchain.db")
    
    # Done with the blockchain database and the database is deleted
    
    # To delete the database, you can use the following code:
    
    # import os
    if os.path.exists("blockchain.db"):
        os.remove("blockchain.db")
        
    # Done with the blockchain database and the database is deleted
    
    # To delete the database, you can use the following code:
    
    # import os
    if os.path.exists("blockchain.db"):
        os.remove("blockchain.db")
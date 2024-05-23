import hashlib
import random
import subprocess
import qrcode

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Création de la blockchain
blockchain = Blockchain()

# Création de la réserve de 21 millions de points
for i in range(21000000):
    blockchain.add_block(Block(i, ""))

# Vérification de la validité de la blockchain
print("La blockchain est valide :", blockchain.is_chain_valid())
def ping_latency(host):
    try:
        output = subprocess.check_output(['ping', '-c', '4', host])
        lines = output.decode().split('\n')
        for line in lines:
            if 'avg' in line:
                latency = line.split('/')[4]
                return float(latency)
    except subprocess.CalledProcessError:
        return None

host = 'example.com'
latency = ping_latency(host)
if latency is not None:
    print(f'Ping latency to {host}: {latency} ms')
else:
    print(f'Failed to ping {host}')
    password_level1 = "password1"
    password_level3 = "password3"

    def combine_security_level3_with_latency(latency):
        if latency is not None:
            if latency > 100:
                # Perform security level 3 actions
                input_password = input("Enter password: ")
                if input_password == password_level3:
                    # Perform actions for security level 3
                    print("Security level 3 actions performed.")
                else:
                    print("Incorrect password.")
            else:
                # Perform security level 1 actions
                input_password = input("Enter password: ")
                if input_password == password_level1:
                    # Perform actions for security level 1
                    print("Security level 1 actions performed.")
                else:
                    print("Incorrect password.")
        else:
            print("Failed to get latency.")

    combine_security_level3_with_latency(latency)
    # Generate QR code for two-factor authentication
    def generate_qr_code(data):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save("qr_code.png")

    # Example data for two-factor authentication
    two_factor_data = "https://example.com/2fa"

    # Generate QR code
    generate_qr_code(two_factor_data)

    # After mining is finished and data deletion is confirmed, send the folder containing the chip
    send_folder_with_chip()
    # Create a list of 10 miners
    miners = []
    for _ in range(10):
        miners.append(Blockchain())

    # Mine on two levels
    for miner in miners:
        for i in range(1000000):
            miner.add_block(Block(i, ""))

    # Record ping latency and approve with 2-factor authentication
    def record_ping_latency_with_qr_code(miner):
        host = 'example.com'
        latency = ping_latency(host)
        if latency is not None:
            print(f'Ping latency to {host}: {latency} ms')
            combine_security_level3_with_latency(latency)
            two_factor_data = f"https://example.com/2fa/{latency}"
            generate_qr_code(two_factor_data)
            # Receive 0.01% of 1 point if mined
            if miner.is_chain_valid():
                receive_reward(0.0001)
        else:
            print(f'Failed to ping {host}')

    # Perform second level mining and data deletion
    def perform_second_level_mining(miner):
        for i in range(1000000):
            miner.add_block(Block(i, ""))
        send_folder_with_chip()
        stop_mining()

    # Perform mining and data deletion for each miner
    for miner in miners:
        record_ping_latency_with_qr_code(miner)
        perform_second_level_mining(miner)
        # Loop over the branches and mine the resource
        for i in range(0, len(miners), 10):
            branch = miners[i:i+10]
            for miner in branch:
                for i in range(1000000):
                    miner.add_block(Block(i, ""))
                send_folder_with_chip()
                stop_mining()
                # Perform two-factor authentication using the main miners as admission masters
                for master_miner in miners[:10]:
                    combine_security_level3_with_latency(ping_latency('example.com'))
                    # Provide 1% of the point amount to the secondary branch
                    if master_miner.is_chain_valid():
                        receive_reward(0.01)
                    else:
                        print("Invalid chain.")
                    # Perform mining and data deletion for each miner
                    


 # Import the necessary libraries
from blockchain import Blockchain

# Create a new Blockchain object

blockchain = Blockchain()

# Define a function that takes in a NFT and returns the metadata for that NFT
# without revealing any of the financial transaction details

def get_nft_metadata(nft_id):

  # Get the block that contains the NFT

  block = blockchain.get_block_containing_nft(nft_id)

  # Extract the NFT from the block and return its metadata

  nft = block.get_nft(nft_id)
  return nft.metadata

# Example usage: get the metadata for NFT with ID 12345
metadata = get_nft_metadata(12345)

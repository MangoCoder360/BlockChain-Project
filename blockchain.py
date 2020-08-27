class Blockchain(object):

	self.new_block(previous_hash=1, proof=100)
	
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self, proof, previous_hash=None):
		#This function creates new blocks and then adds to the existing chain
		pass

	def new_transaction(self):
		self.current_transactions.append(
		{
			‘sender’: sender,

			‘recipient’: recipient

			‘amount’: amount,
		}
	)
	return self.last_block[‘index’] + 1

	@staticmethod
	def hash(block):
		#Used for hashing a block

	@property
	def last_block(self):
		# Calls and returns the last block of the chain
		pass
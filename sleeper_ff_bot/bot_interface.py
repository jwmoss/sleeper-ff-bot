import requests

class botInterface:
	def __init__(self, bot_id):
		self.bot_id = bot_id

	def send_message(self, message):
		'''Will be implemented by each bot class differently '''
		raise NotImplementedError('A send message method has not been implemented')

	def send(self, callback, *args):
		message = callback(*args)
		self.send_message(message)

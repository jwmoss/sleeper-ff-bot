import requests
from bot_interface import botInterface

class GroupMe(botInterface):
	def __init__(self, bot_id):
		self.bot_id = bot_id

	def send_message(self, message):
		requests.post("https://api.groupme.com/v3/bots/post", data={"text":message, "bot_id":self.bot_id} )

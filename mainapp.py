import time
import g_data


class item:
	#
	def __init__(self, item_type):
		self.data = item_type
		self.use = self.data['use']

class data:
	#
	def __init__(self, inventory = 
		[ item(g_data.sword)
		, item(g_data.bag)
		, item(g_data.rope) ]):
		self.inventory = inventory

class game:
	#
	def __init__(self, save_data):
		self.inventory = save_data.inventory
	#
	def inv_print(self):
		print(
			' '.join(
				[ '있는 것은'
				, ', '.join([ looper.data['name'] 
					for looper in self.inventory ])
				, '입니다.' ]))
	#
	def main(self):
		print('무인도에서 살아남기')
		print('------------------')
		print('당신은 이 무인도에서 생존하게 될것이다.')
		print()
		self.inv_print()
	#
	def user_play(self):
		user_input = input('어떤 것을 쓰시겠습니까? : ')
		if user_input:
			for looper in self.inventory:
				if looper.data['name'] == user_input:
					looper.data['use']()
					del looper

now_game = game(data())
now_game.main()
while True:
	now_game.user_play()
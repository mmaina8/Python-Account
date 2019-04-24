class Account:
 
	def __init__(self, first_name,second_name,balance,amount):
		self.first_name = first_name
		self.second_name = second_name
		self.balance = balance
		self.amount = amount

	def welcome (self):
		greeting = "Hello {} {}, welcome to your account. Your current balance is KES {}".format (self.first_name,self.second_name,self.balance)
		return greeting

	def deposit (self):
		deposits = "Hello {} {}, welcome to your account. You have deposited KES {}.".format (self.first_name,self.second_name,self.amount)
		return deposits

	def withdrawal (self):
		withdraw = "Hello {} {}, welcome to your account. You have withdrawn KES {}.".format (self.first_name,self.second_name,self.amount)
		return withdraw
 
	def show_balance (self):
		current = "Hello {} {}, welcome to your account. Your current balance is {}.".format (self.first_name,self.second_name,self.balance-self.amount)
		return current

	
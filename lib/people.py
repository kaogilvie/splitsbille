class Person(object):

	def __init__(self):
		pass

class Payer(Person):

	def __init__(self, name, paid):
		self.name = name
		self.paid = paid
		self.owes = 0
		self.payee = []
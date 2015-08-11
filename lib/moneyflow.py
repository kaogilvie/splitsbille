import csv
import lib.people as people

class Invoice(object):
	"""
	Input of csv in input folder (payers).
	'Name of person', 'positive amount paid'
	"""

	def __init__(self):
		self.invoice_file = './input/payers.csv'
		self.invoice = csv.reader(open(self.invoice_file))
		self.payers = {}

	def calculate_bill(self):
		"""
		Read CSV & instantiate people.
		"""
		self.bottom_line = 0

		for row in self.invoice:
			name = row[0]
			paid = float(row[1])
			self.payers[name]=people.Payer(name, paid)

			self.bottom_line = paid+self.bottom_line

class Bill(object):
	"""
	Input of csv in input folder (owers).
	'Name of person'
	"""
	def __init__(self, invoice_object):
		self.ower_file = './input/owers.csv'
		self.ower_db = csv.reader(open(self.ower_file))
		self.owers = {}
		self.invoice = invoice_object

	def fill_in_extra_owers(self):
		"""
		Creates reference to
		all people who owe money.
		"""
		for row in self.ower_db:
			name = row[0]
			if name not in self.invoice.payers.keys():
				self.invoice.payers[name] = people.Payer(name, 0)

	def calculate_total_owed(self):
		"""
		Take original total and divide by number of
		payers to get the threshhold amount.
		Anyone who has paid less than the threshhold
		owes something; anyone who has paid more will
		receive something.
		"""
		self.owers = {}
		self.receivers = {}
		self.threshhold = self.invoice.bottom_line / len(self.invoice.payers.keys())
		for person in self.invoice.payers.values():
			person.owes = -(person.paid)+self.threshhold
			if person.owes > 0:
				self.owers[person.name]=person
			else:
				self.receivers[person.name]=person
		self.threshhold = self.invoice.bottom_line / len(self.owers.keys())

	def distribute_owed_amount(self):
		"""
		Take the amount that everyone owes
		and distribute it so that each person
		knows who they are paying.
		"""
		for ower in self.owers.values():
			if ower.owes == 0:
				pass
			else:
				for receiver in self.receivers.values():
					print(receiver.name, receiver.owes)

					if receiver.owes == 0:
						print('passed')
						pass

					elif abs(receiver.owes) > abs(ower.owes):
						ower.payee.append(['Pay '+receiver.name+': ', ower.owes])
						receiver.owes = receiver.owes + ower.owes
						ower.owes = 0

					elif abs(receiver.owes) < abs(ower.owes):
						ower.owes = ower.owes - abs(receiver.owes)
						ower.payee.append(['Pay '+receiver.name+' :', -(receiver.owes)])
						receiver.owes = 0

					elif abs(receiver.owes) == abs(ower.owes):
						ower.payee.append(['Pay '+receiver.name+':', ower.owes])
						receiver.owes = receiver.owes + ower.owes
						ower.owes = 0
					

		for ower in self.owers.values():
			print(ower.name,':',ower.payee)

	def write_final_totals_to_csv(self):
		pass
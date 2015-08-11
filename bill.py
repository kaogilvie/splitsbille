import csv
import people

class Invoice(object):
	"""
	Input of csv in input folder.
	'Name of person', 'positive amount paid'
	"""

	def __init__(self):
		self.bill_file = '../input/bill.csv'
		self.bill = csv.reader(open(self.bill_file))
		self.payers = {}

	def calculate_bill(self):
		"""
		Read CSV & instantiate people.
		"""
		self.bottom_line = 0

		for row in self.bill:
			name = row[0]
			paid = int(row[1])
			self.payers[row]=people.Payer(name, paid)

			self.bottom_line = paid+self.bottom_line
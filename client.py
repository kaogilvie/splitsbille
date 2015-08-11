
if __name__ == "__main__":

	from lib import moneyflow

	invoice = moneyflow.Invoice()
	invoice.calculate_bill()

	bill = moneyflow.Bill(invoice)
	bill.fill_in_extra_owers()
	bill.calculate_total_owed()
	bill.distribute_owed_amount()
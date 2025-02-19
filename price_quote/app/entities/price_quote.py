from .i_price_quote import IPriceQuote
from ..helpers import calculate_discount_price, calculate_tax, \
    calculate_items_total_pricing

class PriceQuote(IPriceQuote):
	def __init__(self, request_data):
		self.request_data = request_data
		self.validate_pricing_quote()

	def validate_pricing_quote(self):
		if self.request_data.get('name') and self.request_data.get('price'):
			return True

	def validate_quote_order(self):
		discounts = self.request_data.get("discounts")
		sub_total = self.request_data.get("sub_total")
		items = self.request_data.get("items")
		tax = self.request_data.get("tax")
		total = self.request_data.get("tax")
		if (sub_total and items and total) or tax or discounts:
			calculated_sub_total = calculate_items_total_pricing(items)
			if calculated_sub_total and discounts:
				discounted_subtotal = calculate_discount_price(discounts, calculated_sub_total)
				if discounted_subtotal != sub_total:
					return {
						"message": "sub-total does not tally with summation of item"
					}, 400
				if tax:
					calculated_total_with_tax = calculate_tax(tax, discounted_subtotal)
					if total != calculated_total_with_tax:
						return {
							"message": "total does not tally with summation of item and taxes"
						}, 400

			elif calculated_sub_total and tax and not discounts:
				calculated_total_with_tax = calculate_tax(tax, calculated_sub_total)
				if total != calculated_total_with_tax:
					return {
						"message": "subtotal does not tally with summation of item and taxes"
					}, 400
			elif calculated_sub_total != total:
				return {
					"message": "subtotal does not tally with summation of item"
				}, 400

		return 	{
			"message": "Missing fields: total or sub_total or items"
		}, 400





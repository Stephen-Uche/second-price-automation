from abc import ABCMeta, abstractmethod


class IPriceQuote(metaclass=ABCMeta):
	@abstractmethod
	def validate_pricing_quote(self):
		raise NotImplementedError()

	@abstractmethod
	def validate_quote_order(self):
		raise NotImplementedError()



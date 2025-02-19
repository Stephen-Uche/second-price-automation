from abc import ABCMeta, abstractmethod


class IAdapterFactory(metaclass=ABCMeta):
	@abstractmethod
	def create_pricing_quote_adapter(self):
		raise NotImplementedError()
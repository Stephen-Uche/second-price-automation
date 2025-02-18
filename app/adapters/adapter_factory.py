from .i_adapter_factory import IAdapterFactory

from ..entities import PriceQuote

#Adapter factory created price_quote method.
class AdapterFactory(IAdapterFactory):

	def create_pricing_quote_adapter(self, request_data):
		return PriceQuote(request_data)

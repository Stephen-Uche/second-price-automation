from flask import abort

from ..usecases.i_request import IRequest
from .i_rest import IRest

class RestAdapter(IRequest, IRest):
	def __init__(self, adapter_factory) -> None:
		self.adapter_factory = adapter_factory

	def rest(self, args: dict, **kwargs): # args = request type, kwargs = body
		if args["request"] == "create_price":
				price_to_create = self.create_price(kwargs.get("data"))
				if price_to_create:
					return {
						"message": "price created"
					}, 200
				abort(400)
    
		if args["request"] == "generate_quote":
			# entity = self.adapter_factory.create_pricing_quote_adapter(kwargs.get('data'))
			# validate_quote_message = entity.validate_quote_order()
			# if validate_quote_message:
				# return validate_quote_message
			if self.generate_pricing_quote(kwargs.get('data')):
				return {
					"message": "quotes generated"
				}, 200
			abort(400)

    
		#if args["request"] == "generate_price":
		#		price_to_generate = self.generate_pricing_quote(kwargs.get("data"))
		#		if price_to_generate:
		#			return {
		#				"message": "price generated"
		#			}, 200
		#		abort(400)

  
		if args["request"] == "get_quotes":
			return self.get_quotes_callback()

		if args["request"] == "get_quote_by_id":
			return self.get_quote_by_id_callback(kwargs.get("id"))

		if args["request"] == "get_pricing":
			return self.get_pricing_callback()

		if args["request"] == "get_quote_request":
			return self.get_quote_request_callback()


		if args["request"] == "delete_price_by_id":
				price_to_delete_by_id = self.delete_price_by_id_callback(kwargs.get("data"))
				if price_to_delete_by_id:
					return{
						"message": "price deleted"
					}, 200 
				abort(400)
		
		if args["request"] == "set_quote":
			#quotes_to_update = self.set_quote(kwargs)
			quotes_to_update = self.set_quote(kwargs.get('data'))
			if quotes_to_update:
				return {
					"message": "quotes updated"
				}, 200
			abort(400)
		if args["request"] == "set_price":
			quotes_to_update = self.set_price(kwargs.get('data'))
			if quotes_to_update:
				return {
					"message": "price updated"
				}, 200
			abort(400)    

	def create_price_subscription(self, callback_method):
		self.create_price_callback = callback_method
  

  
	def get_pricing_subscription(self, callback_method):
		self.get_pricing_callback = callback_method
  
	def get_quote_request_subscription(self, callback_method):
		self.get_quote_request_callback = callback_method

   
  
	def get_quotes_subscription(self, callback_method):
		self.get_quotes_callback = callback_method
  
	def get_quote_by_id_subscription(self, callback_method):
		self.get_quote_by_id_callback = callback_method

  
	def generate_pricing_quote_subscription(self, callback_method):
		self.generate_pricing_quote_callback = callback_method
  
	def delete_price_by_id_subscription(self, callback_method):
		self.delete_price_by_id_callback = callback_method


	def set_quote_subscription(self, callback_method):
		self.set_quote_callback = callback_method
  
	def set_price_subscription(self, callback_method):
		self.set_price_callback = callback_method
  
	def create_price(self, kwargs):
		validate_price = self.adapter_factory.create_pricing_quote_adapter(kwargs)
		if validate_price:
			return self.create_price_callback(kwargs)

	def set_price(self, kwargs):
		validate_price = self.adapter_factory.create_pricing_quote_adapter(kwargs)
		if validate_price:
			return self.set_price_callback(kwargs)

	def set_quote(self, kwargs):
		validate_quote = self.adapter_factory.create_pricing_quote_adapter(kwargs)
		if validate_quote:
			return self.set_quote_callback(kwargs)

	def generate_pricing_quote(self, kwargs):
		return self.generate_pricing_quote_callback(kwargs)

	#def get_quote_by_id(self, kwargs):
	#	return self.get_quote_by_id_callback(kwargs, id)



	

from .i_usecase_factory import IUsecaseFactory

from ..adapters.models.price_quote_model import PriceQuote as PriceQuoteModel, \
    QuoteRequest as QuoteRequestModel,\
    QuoteOrder as QuoteOrderModel
    
class PricingQuote:
    def __init__(self, usecase_factory:IUsecaseFactory):
        self.usecase_factory = usecase_factory 
        self.request = usecase_factory.create_request() #RestAdapter
        self.pricing_quote = usecase_factory.create_quotes() #DataAdapter
        self.object = usecase_factory.create_object() #Filehandler
        self.object_generated_path = 'generated'# TODO: create absolute path/folder
        
        self.price_quote_model_class = PriceQuoteModel
        self.quote_request_model_class = QuoteRequestModel
        self.quote_order_model_class = QuoteOrderModel
        
        self.get_resources()
        self.subscribe_to_requests()
        
    def get_resources(self):
        self.pricing = self.pricing_quote.get_pricing(self.price_quote_model_class)
        self.quote_request = self.pricing_quote.get_quote_request(self.quote_request_model_class)
        self.quotes = self.pricing_quote.get_quotes(self.quote_order_model_class)
        #self.quotes = self.pricing_quote.get_quotes(self.quote_request_model_class)

    
    def subscribe_to_requests(self):
        self.request.get_quotes_subscription(self.get_quotes_callback)
        self.request.get_quote_by_id_subscription(self.get_quote_by_id_callback)
        self.request.get_pricing_subscription(self.get_pricing_callback)
        self.request.get_quote_request_subscription(self.get_quote_request_callback)
        self.request.create_price_subscription(self.create_price_callback)
        self.request.generate_pricing_quote_subscription(self.generate_pricing_quote_callback)
        self.request.set_quote_subscription(self.set_quote_callback)
        self.request.set_price_subscription(self.set_price_callback)
        self.request.delete_price_by_id_subscription(self.delete_price_by_id_callback)
        
    def create_price_callback(self, price: dict):            
        return self.pricing_quote.create_price(price, self.price_quote_model_class)
    
    def generate_pricing_quote_callback(self, data: dict):
        title = data.get("title")
        customer_name = data.get("customer_name")
        created_by_id = data.get("created_by_id") 
        comments = data.get("comments")
        delivery_period = data.get("delivery_period")
        discounts = data.get("discounts")
        sub_total = data.get("sub_total")
        tax: float = data.get("tax")
        total = data.get("total")
        items = data.get("items")
        
        order_id = self.quote_order_model_class.generate_order_id(),
        add_order = {
            "created_by_id": created_by_id, 
	        "title": title,
	        "order_id": order_id,
	        "customer_name": customer_name,
	        "tax": tax,
	        "sub_total": sub_total,
	        "discounts": discounts,
	        "comments": comments, 
	        "delivery_period": delivery_period
        }
        order = self.pricing_quote.create_order(add_order, self.quote_order_model_class)
        _order_id = order.id
                
        order_requests =[]
        for price in items:
            _price_id = price.get("id")
            _price_qty = price.get("quantity")
            price_quote = self.price_quote_model_class.id_exists(_price_id)
            if price_quote:
                add_order_request_data = {
                    "quote_order_id": _order_id,
                    "price_quote_id": _price_id,
                    "quantity": _price_qty
                }
                
                order_requests.append(add_order_request_data)
                
        body = {
            "data":{
                "order_id": _order_id,
                "comments": comments,
		        "created_by_id": created_by_id,
		        "customer_name": customer_name,
		        "delivery_period": delivery_period,
		        "discounts": discounts,
		        "sub_total": sub_total,
		        "tax": tax,
		        "title": title,
		        "total": total,
		        "items": items
            }
            
        }
        self.pricing_quote.create_quote_request(add_order_request_data, self.quote_request_model_class)
        filename = f"{data['customer_name']}-qoutation.pdf"
        self.object.convertHtmlToPdf(body["data"], filename)
        return {"message": "created PDF"}
    
    
    
    def get_quote_by_id_callback(self, id):
        return self.pricing_quote.get_quote_by_id(self.quote_order_model_class, id)
        
    
    def get_quotes_callback(self):
        return self.quotes
        

    
    def get_pricing_callback(self):
        return self.pricing
    
    def get_quote_request_callback(self):
        return self.quote_request

    
    def set_quote_callback(self, quote: dict):
        return self.pricing_quote.set_quote(quote, self.quote_order_model_class)
    
    def set_price_callback(self, price: dict):
        return self.pricing_quote.set_price(price, self.price_quote_model_class)
    
    def delete_price_by_id_callback(self, id):
        return self.pricing_quote.delete_price_by_id(self.price_quote_model_class, id)



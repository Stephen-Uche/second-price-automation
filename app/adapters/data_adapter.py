import dataclasses

#from flask_migrate import Migrate
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
# from usecases.i_pricing_quote import IPricingQuote


from ..usecases.i_pricing_quote import IPricingQuote


@dataclasses.dataclass
class DataAdapter(IPricingQuote):
    def __init__(self, data_source):
        self.data_source = data_source   

    def create_price(self, price: dict, model_class):
        return self.data_source.write(model_class, price)
    
    def create_quote(self, quote: dict, model_class):
        return self.data_source.write(model_class, quote)
    
    def create_order(self, order: dict, model_class):
        return self.data_source.write(model_class, order)
    
    def create_quote_request(self, data: dict, model_class):
        return self.data_source.write(model_class, data)
    
    def get_quote_by_id(self, model_class, id) -> dict:
        return self.data_source.read_by_id(model_class, id)
    
    def get_quotes(self, model_class) -> list:
        return self.data_source.read(model_class)
    
    def get_pricing(self, model_class) -> list:
        return self.data_source.read(model_class)
    
    def get_quote_request(self, model_class) -> list:
        return self.data_source.read(model_class)            
            

    def set_quote(self, quote: dict, model_class):
        return self.data_source.update(model_class, quote)
        
    def set_price(self, price: dict, model_class):
        return self.data_source.update(model_class, price)

    def set_quotes(self, quotes: list, model_class):
        for quote in quotes:
            self.set_quote(quote, model_class)
        return quotes
    
    def delete_price_by_id(self, model_class, id: int) -> int:
        return self.data_source.delete(model_class, id=id)


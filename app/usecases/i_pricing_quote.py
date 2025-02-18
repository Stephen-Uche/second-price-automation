from abc import ABCMeta, abstractmethod

class IPricingQuote(metaclass=ABCMeta):
    @abstractmethod
    def create_price(self, price: dict, model_class):
        raise NotImplementedError()
    
    @abstractmethod
    def create_quote(self, quote: dict, model_class):
        raise NotImplementedError()

    
    @abstractmethod
    def get_quote_by_id(self, id)-> dict:
        raise NotImplementedError()
    
    @abstractmethod
    def get_quotes(self)-> list:
        raise NotImplementedError()
    
    @abstractmethod
    def get_pricing(self)-> list:
        raise NotImplementedError()
    
    @abstractmethod
    def get_quote_request(self)-> list:
        raise NotImplementedError()

     
    @abstractmethod
    def set_quote(self, arg:dict):
        raise NotImplementedError()
    
    @abstractmethod
    def set_price(self, arg:dict):
        raise NotImplementedError()
    
    @abstractmethod
    def delete_price_by_id(self, model_class, id) -> dict:
        raise NotImplementedError()

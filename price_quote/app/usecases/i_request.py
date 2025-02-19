from abc import ABCMeta, abstractmethod

class IRequest(metaclass=ABCMeta):
    
    @abstractmethod
    def create_price_subscription(self, callback):
        raise NotImplementedError
    
    #@abstractmethod
    #def create_quote_subscription(self, callback):
        #raise NotImplementedError

    
    @abstractmethod
    def get_quotes_subscription(self, callback_method):
        raise NotImplementedError
    
    @abstractmethod
    def get_quote_by_id_subscription(self, callback_method):
        raise NotImplementedError

    
    @abstractmethod
    def get_pricing_subscription(self, callback_method):
        raise NotImplementedError
    
    @abstractmethod
    def generate_pricing_quote_subscription(self, args:dict):
        raise NotImplementedError
    
    @abstractmethod
    def set_quote_subscription(self, args:dict):
        raise NotImplementedError
    
    @abstractmethod
    def set_price_subscription(self, args:dict):
        raise NotImplementedError
from abc import ABCMeta, abstractmethod

class IRest(metaclass=ABCMeta):
    
	@abstractmethod
	def rest(self, args: dict, **kwags):
		raise NotImplementedError()
	
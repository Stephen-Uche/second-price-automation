from abc import ABCMeta, abstractmethod

class IDataSource(metaclass=ABCMeta):
    
	@abstractmethod
	def read(self, model_class, read_first: bool):
		raise NotImplementedError()
	

	@abstractmethod
	def read_by_id(self, model_class, id: int):
		raise NotImplementedError()
	

	@abstractmethod
	def update(self, model_class, args: dict):
		raise NotImplementedError()
	

	def write(self, model_class, args: dict):
		raise NotImplementedError()


	def delete(self, model_class, id: int):
		raise NotImplementedError()


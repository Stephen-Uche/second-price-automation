from ..usecases.i_usecase_factory import IUsecaseFactory
from .adapter_factory import AdapterFactory
from .rest_adapter import RestAdapter
from .data_adapter import DataAdapter
from .file_handler import FileHandler

class UsecaseFactory(IUsecaseFactory):
	def __init__(self, data_source):
		self.data_source = data_source # sqlalchemy_adapater
		self.adapter_factory = AdapterFactory()
		self.rest_adapter = RestAdapter(self.adapter_factory) # We want one instance of RestAdapter
		self.object = FileHandler()
		print("usecase factory created!")

	def create_request(self):
		return self.rest_adapter
	
	def create_quotes(self):
		return DataAdapter(self.data_source)

	def create_object(self):
		return self.object
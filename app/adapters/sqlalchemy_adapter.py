import sys
from flask import jsonify

from .i_data_source import IDataSource
from .models.price_quote_model import PriceQuote

class SqlAlchemyAdapter(IDataSource):
	def __init__(self, sqlalchemy) -> None:
		self.sqlalchemy = sqlalchemy


	def get_method(self, class_name: str):
		try:
			return getattr(sys.modules[__name__], class_name)
		except:
			raise ValueError("Class {} not found.".format(class_name))


	def write(self, model_class, args: dict):
		try:
			data_to_write = model_class(**args)
			self.sqlalchemy.session.add(data_to_write)
			self.sqlalchemy.session.commit()
			return data_to_write
			
		except Exception as e:
			self.sqlalchemy.session.rollback()
			raise e
	
	
	def read_first(self, model_class):
		return model_class.query.first()


	def read(self, model_class, read_first=False):
		try:
			if read_first:
				return model_class.query.first()
			else:
			# usecase_model = self.get_method(model_class)
				data = model_class.query.all()
				return jsonify([_data.to_json() for _data in data])
		except Exception as e:
			print('no database found')

	def read_by_id(self, model_class, id):
		return  model_class.query.get_or_404(id)


	def update(self, model_class, args: dict):
		try:
			_id = args.get('id')
			print("------------", _id)
			if _id:
				# usecase_model_to_update = self.get_method(model_class)
				data_to_update = self.read_by_id(model_class, _id)
				for key, value in args.items():
					if hasattr(data_to_update, key):
						setattr(data_to_update, key, value)
				self.sqlalchemy.session.commit()
				return data_to_update

		except Exception as e:
			self.sqlalchemy.session.rollback()
			raise e

	def delete(self, model_class, id: int):
		data_to_delete = self.read_by_id(model_class, id)

		self.sqlalchemy.session.delete(data_to_delete)
		self.sqlalchemy.session.commit()
		return True

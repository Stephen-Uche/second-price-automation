import threading
from datetime import datetime

from datetime import datetime
from app.db import sqlalchemy

lock = threading.Lock()
class PriceQuote(sqlalchemy.Model):
	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	name = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
	price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
	description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
	created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
	updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)
	
	quote_request = sqlalchemy.relationship('QuoteRequest', backref='price_quote', lazy='dynamic', passive_deletes=True)

	def __repr__(self):
		return '<PriceQuote {}>'.format(self.description)
	
	@classmethod
	def id_exists(cls, id):
		return cls.query.get(id)

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name,
			'price': self.price,
			'description': self.description,
		}
  
class QuoteOrder(sqlalchemy.Model):

	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	order_id = sqlalchemy.Column(sqlalchemy.String(20), nullable=False)
	created_by_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
	title = sqlalchemy.Column(sqlalchemy.String(255), nullable=True)
	customer_name = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
	sub_total = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
	total = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
	tax = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
	discounts = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
	vat = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
	comments = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
	delivery_period = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
	created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
	updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)
	
	quote_request = sqlalchemy.relationship('QuoteRequest', backref='quote_order', lazy='dynamic', passive_deletes=True)

	def __repr__(self):
		return {
			'id': self.id,
			'order_id': self.order_id,
    		'created_by_id': self.created_by_id,
			'title': self.title,
			'customer_name': self.customer_name,
    		'sub_total': self.sub_total,
    		'total': self.total,
    		'tax': self.tax,
    		'discounts': self.discounts,
    		'vat': self.vat,
    		'comments': self.comments,
			'delivery_period': self.delivery_period,
		}

	@staticmethod
	def generate_order_id():
		with lock:
			today = datetime.now().strftime('%Y%m%d')  # Date format: YYYYMMDD
			last_order = QuoteOrder.query.order_by(QuoteOrder.order_id.desc()).first()
			last_id = last_order.order_id if last_order else f"{today}0104"
			date, num = last_id[:8], int(last_id[8:])
			new_id = f"{today}{num+1:04d}" if date == today else f"{today}0105"
			return new_id

	def to_json(self):
		return {
			'id': self.id,
			'order_id': self.order_id,
            'created_by_id': self.created_by_id,
			'title': self.title,
			'customer_name': self.customer_name,
            'sub_total': self.sub_total,
            'total': self.total,
            'tax': self.tax,
            'discounts': self.discounts,
            'vat': self.vat,
            'comments': self.comments,
			'delivery_period': self.delivery_period,
		}

class QuoteRequest(sqlalchemy.Model):
	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
	quote_order_id = sqlalchemy.Column(sqlalchemy.Integer,  sqlalchemy.ForeignKey(QuoteOrder.id, ondelete='CASCADE'))
	price_quote_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(PriceQuote.id, ondelete='CASCADE'))
	created_by_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
	quantity = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
	created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)
	updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return '<QuoteRequest {}>'.format(self.description)


	def to_json(self):
		return {
			'id': self.id,
			'quote_order_id': self.quote_order_id,
			'price_quote_id': self.price_quote_id,
            'created_by_id': self.created_by_id,
            'quantity': self.quantity,
		}

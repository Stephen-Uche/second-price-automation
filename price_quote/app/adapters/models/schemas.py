# app/schemas.py
from marshmallow import validate

from app.db import ma
from .price_quote_model import PriceQuote, QuoteRequest, QuoteOrder
    

class PriceQuoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PriceQuote
        description = 'This schema represents a price_quote automation'
        
    id = ma.auto_field(dump_only=True)
    name = ma.String(required=True)
    price = ma.Float(required=True)
    description = ma.String(required=False)    

class UpdatePriceQuoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PriceQuote
        
    id = ma.Integer(required=True)
    name = ma.String(required=True)
    price = ma.Float(required=True)
    description = ma.String(required=False)
    

class QuoteRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = QuoteRequest
        description = 'This schema represents a quote_request automation'
        
    id = ma.auto_field(dump_only=True)
    quote_order_id = ma.Integer(required=True)
    price_quote_id = ma.Integer(required=True)
    created_by_id = ma.Integer(required=True)
    quantity = ma.Integer(required=True)    

class UpdateQuoteRequestSchema(ma.SQLAlchemySchema):
    class Meta:
        model = QuoteRequest
        
    id = ma.Integer(required=True)
    quote_order_id = ma.Integer(required=True)
    price_quote_id = ma.Integer(required=True)
    created_by_id = ma.Integer(required=True)
    quantity = ma.Integer(required=True)    


class QuoteOrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = QuoteOrder
        description = 'This schema represents a quote_order automation'
        
    id = ma.auto_field(dump_only=True)
    order_id = ma.Integer(dump_only=True)
    created_by_id = ma.Integer(required=True)
    title = ma.String(required=True)
    customer_name = ma.String(required=True)
    sub_total = ma.Float(required=True)
    tax = ma.Float(required=False)
    discounts = ma.Float(required=False)
    total = ma.Float(required=True)
    comments = ma.String(required=False)
    delivery_period = ma.String(required=True)
    
    items = ma.List(ma.Dict(ma.String, ma.Raw), required=True)
    
        

class UpdateQuoteOrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = QuoteOrder
        
    id = ma.Integer(required=True)
    order_id = ma.Integer(required=True)
    created_by_id = ma.Integer(required=True)
    customer_name = ma.String(required=True)
    items = ma.List(ma.Dict(ma.String, ma.Raw), required=True)
    sub_total = ma.Float(required=True)
    tax = ma.Float(required=True)
    discounts = ma.Float(required=True)
    vat = ma.Float(required=True)
    comments = ma.String(required=False)
    delivery_period = ma.String(required=True)

from .adapters import UsecaseFactory, AdapterFactory, SqlAlchemyAdapter
from .entities import PriceQuote, IPriceQuote
from .usecases import PricingQuote

import os, logging, pathlib
from flask import Flask, Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from datetime import datetime

from apifairy import body, response, other_responses
from .db import sqlalchemy, ma

def setup_log():
    dt = datetime.now() 
    date_format = dt.strftime("%Y-%m-%d")
    logs_path = pathlib.Path(__file__).parent.resolve() / "logs"

    if not logs_path.is_dir():
        os.makedirs(logs_path)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(pathname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=f"logs/pricing_quote-{date_format}.log",
    )

sqlalchemy_adapater = SqlAlchemyAdapter(sqlalchemy)
migrate = Migrate(compare_type=True)

route_blueprints = Blueprint('route_blueprints', __name__)

def create_blueprint(app):
	app.register_blueprint(route_blueprints, url_prefix="/pricing_quote/v1")
	return app



def register_routes(rest_adapter):
    from .adapters.models.schemas import PriceQuoteSchema, UpdatePriceQuoteSchema, \
        UpdateQuoteRequestSchema, QuoteOrderSchema, UpdateQuoteOrderSchema
    @route_blueprints.route('/')
    def health_check():
        return jsonify({"message": "price_quote API Module"})
    
    @route_blueprints.route('/<int:id>', methods=['GET'])
    @response(QuoteOrderSchema)
    def get_quote_by_id_subscription(id):
        #data = {'id': id} #TODO: send a hashed id and decipher 
        return rest_adapter.rest({"request": "get_quote_by_id"}, id=id)
    
    @route_blueprints.route('/prices', methods=['GET'])
    def get_pricing_subscription():
        return rest_adapter.rest({"request": "get_pricing"})
    
    @route_blueprints.route('/requests', methods=['GET'])
    def get_quote_request_subscription():
        return rest_adapter.rest({"request": "get_quote_request"})

    
    @route_blueprints.route('/quotes', methods=['GET'])
    def get_quotes_subscription():
        return rest_adapter.rest({"request": "get_quotes"})

    

    @route_blueprints.route('/price', methods=['POST'])
    @body(PriceQuoteSchema)
    @other_responses({400: 'Bad Request'})
    @other_responses({401: 'Unauthorized'})
    def create_price_subscription(price):
        return rest_adapter.rest(args={"request": "create_price"}, data=price)
    
    @route_blueprints.route('/quote', methods=['POST'])
    @body(QuoteOrderSchema)
    @other_responses({400: 'Bad Request'})
    @other_responses({401: 'Unauthorized'})
    def generate_pricing_quote_subscription(quote):
        return rest_adapter.rest(args={"request": "generate_quote"}, data=quote)

    
    @route_blueprints.route('/price', methods=['PATCH'])
    @body(UpdatePriceQuoteSchema)
    @other_responses({400: 'Bad Request'})
    @other_responses({401: 'Unauthorized'})
    def set_price_subscription(price):
        return rest_adapter.rest(args={"request": "set_price"}, data=price)

    
    @route_blueprints.route('/quote', methods=['PATCH'])
    #@body(UpdateQuoteRequestSchema)
    @body(UpdateQuoteOrderSchema)
    @other_responses({400: 'Bad Request'})
    @other_responses({401: 'Unauthorized'})
    def set_quote_subscription(quote):
        return rest_adapter.rest(args={"request": "set_quote"}, data=quote)
    
    @route_blueprints.route("/<int:id>", methods=["DELETE"])
    def delete_price_by_id(id):
        return rest_adapter.rest({"request": "delete_price_by_id"}, data=id)


def create_flask_app(config_class)-> Flask:
    app = Flask(__name__)

    app.config.from_object(config_class)
    # CORS(app, support_credentials=True)

    with app.app_context():
        sqlalchemy.init_app(app)
        ma.init_app(app)

        migrate.init_app(app, sqlalchemy)
        usecase_factory = UsecaseFactory(sqlalchemy_adapater)
        pricing_quote = PricingQuote(usecase_factory)

        rest_adapter = usecase_factory.create_request()
        register_routes(rest_adapter)

        create_blueprint(app)
        return app

from .adapters.models.price_quote_model import PriceQuote as PriceQuoteModel, QuoteOrder, QuoteRequest

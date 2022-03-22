#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from urllib import response
from flask import Flask
from flask_restx import Api, Resource, reqparse

flask_app = Flask(__name__)
api_app = Api(
    app = flask_app, 
    title="my python application",
    description="hello world",
    version="1.0",
)
logger = flask_app.logger

admin_namespace = api_app.namespace('admin', description='Admin APIs')

# demo
@admin_namespace.route("/<string:id>")
@admin_namespace.doc(params={'id': 'An ID'})
class AdminRoute(Resource):
    @admin_namespace.doc(responses={200: 'ok', 400: 'param invalid'})
    def get(self, id):
        logger.info("[AdminRoute.get] id: {}".format(id))
        return {'hello': 'admin'}

# multiple endpoint
endpoint_namespace = api_app.namespace('endpoint', description='Endpoint APIs')
@endpoint_namespace.route('/', '/bak')
class EndPoint(Resource):
    @endpoint_namespace.doc(responses={200: 'ok', 400: 'param invalid'})
    def get(self):
        logger.info("[Endpoint.get]")
        return {'hello': 'endpoint'}

# parse args (reqparse)
parse_namespace = api_app.namespace('parse', description='with parse args APIs')
id_parser = reqparse.RequestParser()
id_parser.add_argument('arg_id1', type=int, help='add id with int')
id_parser.add_argument('arg_id2', type=int, help='add id with int')
@parse_namespace.route('/<string:id>')
@parse_namespace.doc(params={'id': 'String ID'})
class Parse(Resource):
    @parse_namespace.doc(responses={200: 'ok', 400: 'param invalid'})
    @parse_namespace.doc(parser=id_parser)
    def get(self, id):
        logger.info("[Parser.get]")
        args = id_parser.parse_args()
        id1 = args['arg_id1']
        id2 = args['arg_id2']
        return "Args: id1: {}, id2: {}".format(id1, id2)

# parse args (marshmallow)
marsh_namespace = api_app.namespace('marsh', description='with parse args APIs')
id_parser = reqparse.RequestParser()
id_parser.add_argument('arg_id1', type=int, help='add id with int')
id_parser.add_argument('arg_id2', type=int, help='add id with int')
@parse_namespace.route('/<string:id>')
@parse_namespace.doc(params={'id': 'String ID'})
class Parse(Resource):
    @parse_namespace.doc(responses={200: 'ok', 400: 'param invalid'})
    @parse_namespace.doc(parser=id_parser)
    def get(self, id):
        logger.info("[Parser.get]")
        args = id_parser.parse_args()
        id1 = args['arg_id1']
        id2 = args['arg_id2']
        return "Args: id1: {}, id2: {}".format(id1, id2)

# field mask
from flask_restx import fields
api_req_model = api_app.model('Model', {
    'id': fields.Integer,
    'name': fields.String,
})
mask_namespace = api_app.namespace('mask', description='Mask APIs')
@mask_namespace.route("/")
class MaskRoute(Resource):
    @mask_namespace.doc(responses={200: 'ok', 400: 'param invalid'})
    @api_app.marshal_with(api_req_model)
    def get(self):
        logger.info("[MaskRoute.get]")
        return {'hello': 'model', 'name': 'mask_name'}

# sub url (class)

if __name__ == '__main__':
    # from waitress import serve
    # serve(flask_app, host="0.0.0.0", port=5000, debug=True)
    ## todo: 增加启动参数，设置 debug or 正式环境模式
    flask_app.run(debug=True, host="0.0.0.0", port=5000)


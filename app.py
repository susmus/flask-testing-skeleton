#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.restful import Api, Resource
import os

app = Flask(__name__)
config = os.environ.get('FLASK_CONFIG')
if not config:
    config='debug'
app.config.from_object('config.{}Config'.format(config.capitalize()))

api = Api(app)

class BaseUrl(Resource):
    def get(self):
        return {'message': 'hello GET'}, 200

    def post(self):
        return {'message': 'hello POST'}, 200

    def put(self):
        return {'message': 'hello PUT'}, 200

    def delete(self):
        return {'message': 'hello DELETE'}, 403

api.add_resource(BaseUrl, '/')


if __name__ == '__main__':
    app.run()

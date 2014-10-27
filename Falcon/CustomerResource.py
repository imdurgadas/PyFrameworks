__author__ = 'durgadas_kamath'

import falcon
import json

class CustomerResource(object):

    def on_get(self,req,res):
        res.status = falcon.HTTP_200
        res.body = "All Customers listed !!!!!!!!!!!!"


    def on_post(self,req,resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400,'Error',ex.message)

        try:
            result_json = json.loads(raw_json, encoding='utf-8')
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_400,'Malformed JSON .Could not decode the request body. The JSON was incorrect.')

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result_json, encoding='utf-8')
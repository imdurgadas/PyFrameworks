__author__ = 'durgadas_kamath'

from webob import Response
from webob import exc
from webob.dec import wsgify
from paste import httpserver
from paste.deploy import loadapp
import config
import os

config.CONF(default_config_files=['test.conf'])

@wsgify
def application(req):
    print ("--------- Printing values from conf files : oslo.config -------------- ")
    print ('Enable: {}'.format(config.CONF.durgadas.enable))
    print ("Name =  {} ".format(config.CONF.durgadas.name))
    print ("Passion = {}".format(config.CONF.durgadas.passion))


    res = Response('Yiepeeee.... You have successfully got here !!!!!!!!!! ')
    res.status = 200

    return res


def app_factory(global_config, **local_config):
    print ("global_config %s " % global_config)

    #Iterating over the configs passed from the paste-ini file
    if local_config is not None:
        for key, value in local_config.iteritems():
            print ("%s = %s" % (key, value))

    return application


@wsgify.middleware()
def auth_filter(req, app):
    print "Inside auth_filter"
    #Only allow requests from admin_token whose value is in the conf file

    if req.headers.get('X-Auth-Token') != config.CONF.token.admin_token:
        return exc.HTTPForbidden()

    return app(req)


def auth_factory(global_config, **local_config):
    return auth_filter


paste_loc = 'config:' + os.path.abspath(os.path.dirname(__file__)) + "\\paste.ini"
wsgi_app = loadapp(paste_loc)
httpserver.serve(wsgi_app, host='127.0.0.1', port=8080)
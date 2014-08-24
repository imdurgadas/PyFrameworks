__author__ = 'durgadas_kamath'

from webob import Response
from webob import Request
from webob.dec import wsgify
from paste import httpserver
from paste.deploy import loadapp
import config

config.CONF(default_config_files=['test.conf'])


@wsgify
def application(req):
    res = Response('Trying out stuffs using WSGI paste-deploy ~ durgadas')
    res.status = 201
    print res
    return res


def app_factory(global_config, **local_config):
    print ("global_config %s " % global_config)
    if local_config is not None:
        for key, value in local_config.iteritems():
            print ("%s = %s" % (key, value))

    return application


@wsgify.middleware()
def my_filter1(req, app):
    print "my filter1 was called ..."
    print ('Enable: {}'.format(config.CONF.test.enable))
    return app(req)


@wsgify.middleware()
def my_filter2(req, app):
    print "my filter2 was called ..."
    print ("Name =  {} ".format(config.CONF.durgadas.name))
    print ("Passion = {}".format(config.CONF.durgadas.passion))

    return app(req)


def filter_factory1(global_config, **local_config):
    return my_filter1


def filter_factory2(global_config, **local_config):
    return my_filter2


wsgi_app = loadapp('config:D:/Prog_Development/github/PyFrameworks/MiddlewareApp/src/paste.ini')
httpserver.serve(wsgi_app, host='127.0.0.1', port=8080)
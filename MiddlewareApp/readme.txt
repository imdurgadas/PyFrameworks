[app:main]
paste.app_factory = app:app_factory

When introduced filter, replaced app:main with pipeline:main and created a section app:myapp


We have used 3 concepts here
1. WebOb
2. paste-deploy
3. oslo.config

WebOb WSGI request and response objects
What is it?
 - WebOb is a Python library that provides wrappers around the WSGI request environment, and an object to help create WSGI responses.
 - This helps you create rich applications and valid middleware without knowing all the complexities of WSGI and HTTP.


Paste-Deployment
 - system for finding and configuring WSGI applications and servers.
 - For WSGI application consumers it provides a single, simple function (loadapp) for loading a WSGI application from a configuration
   file or a Python Egg.


oslo.config
 - An OpenStack library for parsing configuration options from the command line and configuration files.
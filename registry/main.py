import os, sys
import argparse
from gunicorn.app.wsgiapp import WSGIApplication
from gunicorn.config import Config
from django.core.management import call_command
from django.core.handlers import wsgi


class BowerRegistryWSGIApplication(WSGIApplication):

    def __init__(self, opts):
        self.bind = "127.0.0.1:{}".format(opts.port or 8000)
        self.cfg = Config()
        # self.cfg.bind = self.bind

    @property
    def callable(self):
        self.chdir()
        settings = 'registry.settings.prod'
        os.environ['DJANGO_SETTINGS_MODULE'] = settings
        try:
            call_command('syncdb', verbosity=0, interactive=False)
            call_command('migrate', verbosity=0, interactive=False)
        except Exception as e:  # because I have to, due to some weird post migrate something or other
            print e
            pass
        from django.contrib.staticfiles.handlers import StaticFilesHandler
        return StaticFilesHandler(wsgi.WSGIHandler())


def run(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, required=False, help="Port Number")

    BowerRegistryWSGIApplication(parser.parse_args()).run()

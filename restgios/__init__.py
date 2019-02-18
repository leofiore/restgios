from restgios.nagios import Nagios
from inotify_simple import INotify, flags
from argparse import ArgumentParser
import tornado.web
import tornado.ioloop
from pathlib import Path
from threading import Thread

cached_services = {}


def notifications(path):

    nag = Nagios()

    watchdir = str(Path(path).parent)
    watchfile = str(Path(path).name)

    watchdog = INotify()
    watch_flags = flags.MOVED_TO
    watchdog.add_watch(watchdir, watch_flags)

    nag.loads(path)
    for service, status in nag.get_services('*'):
        cached_services[service] = status

    while True:
        for event in watchdog.read(1000): # 1000 msecs timeout
            if event.name == watchfile:
                nag.loads(path)

            for service, status in nag.get_services('*'):
                cached_services[service] = status


class Index(tornado.web.RequestHandler):

    def get(self, **params):
        self.write(cached_services)


def main():

    parser = ArgumentParser()

    parser.add_argument("-p", dest="server_port", nargs='?', type=int, default=8979)
    parser.add_argument("-s", dest="status_path", nargs='?', type=str, default="/var/cache/nagios3/status.dat")

    settings = parser.parse_args()

    Thread(target=notifications, args=(settings.status_path,)).start()

    app = tornado.web.Application([
        (r"/", Index),
    ], debug=True)
    app.listen(settings.server_port)
    tornado.ioloop.IOLoop.current().start()

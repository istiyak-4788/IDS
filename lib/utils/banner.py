import time

from colorama import Fore, Style

from lib import __version__ as version

class Banner:
    r = Fore.RED
    y = Fore.YELLOW
    ny = Fore.YELLOW
    nw = Fore.WHITE
    g = Fore.GREEN
    e = Style.RESET_ALL

    def banner(self):
        print("CrossLog: Web Application Security Scanner")

    @classmethod
    def preamble(cls, url):
        print('URL: %s' % url)
        print('---------  Scan Started: %s ---------' % (time.strftime('%d/%m/%Y %H:%M:%S')))

    @classmethod
    def postscript(cls):
        print('---------  Scan Finished: %s ---------' % (time.strftime('%d/%m/%Y %H:%M:%S')))

    def version(self):
        return self.g + "~/#" + self.e + " CrossLog (" + version + ")\n"

from colorama import Fore, Style


class Output:
    r = Fore.RED
    g = Fore.GREEN
    y = Fore.YELLOW
    w = Fore.WHITE
    c = Fore.CYAN
    e = Style.RESET_ALL

    def __init__(self, level=0):
        self.level = level

    def finding(self, value):
        print(
            "{}".format(value),
            flush=True,
        )

    def error(self, value):
        print(
            "{}".format(value),
            flush=True,
        )

    def info(self, value):
        print(
            "{}".format(value),
            flush=True,
        )

    def debug(self, value):
        if self.level == 1:
            print(
                "{}".format(value),
                flush=True,
            )

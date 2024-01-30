class Color:
    @staticmethod
    def red(text):
        print("\033[31m{}\033[0m".format(text))

    @staticmethod
    def green(text):
        print("\033[32m{}\033[0m".format(text))

    @staticmethod
    def yellow(text):
        print("\033[33m{}\033[0m".format(text))

    @staticmethod
    def blue(text):
        print("\033[34m{}\033[0m".format(text))

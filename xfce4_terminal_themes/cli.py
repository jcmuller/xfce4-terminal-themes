from sys import exit
import argparse
from . import configurator

def main():
    c = configurator.Configurator()

    def parse_options():
        parser = argparse.ArgumentParser(description="Configure Xfce4")
        parser.add_argument('theme', help='theme name', choices=c.theme_names, nargs='?')
        parser.add_argument('-l', '--themes', help='list theme names', action='store_true')
        parser.add_argument('-c', '--current', help='display current theme', action='store_true')
        parser.add_argument('-V', '--version', action='version', version=c.version())

        return parser.parse_args()

    args = parse_options()

    if args.themes:
        print("\n".join(c.theme_names))
        exit(0)

    if args.theme:
        c.set_theme(args.theme)
        c.save_config()
        exit(0)

    c.display_config()

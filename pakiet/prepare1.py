import argparse
import configparser
import sys


def main(number, other_number, output):
    result = number * other_number
    print(f"Result: {result}", file=output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n1", help="number to multiply", type=int, default=1)
    parser.add_argument("-n2", help="number to multiply", type=int, default=1)
    parser.add_argument('--config', '-c', help='path to config file', type=argparse.FileType('r'))
    parser.add_argument('-o', help='plik na dane wynikowe', type=argparse.FileType('w'), dest='output',
                        default=sys.stdout)

    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config['ARGS']['n1'])
        args.n2 = int(config['ARGS']['n2'])
    main(args.n1, args.n2, args.output)

import yaml

from spamdetector import app, cli


def main(args=None):
    with open('config.yaml') as f:
        config: dict = yaml.safe_load(f)

    args = cli.parse_args(args, config)

    app(args.file, args.wordlist, args.ignore_headers, args.ignore_body, args.verbose, args.output_format)


if __name__ == '__main__':
    main()

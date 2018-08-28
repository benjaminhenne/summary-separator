from collections import defaultdict
from pathlib import Path

import sys
import argparse
import tensorflow as tf


def setup_argparse():
    parser = argparse.ArgumentParser(description='Script to split up TensorFlow \
    summaries into different files based on their summary tag.')
    parser.add_argument('-f', '--file',
                        help='TensorFlow summary file',
                        required='True')
    parser.add_argument('-t', '--tags',
                        help='list of summary tags to filter out, separated by comma',
                        default='all')
    parser.add_argument('-o', '--output',
                        help='output directory',
                        default='./summary_data/')
    return parser


def main(argv):
    parser = setup_argparse()
    args = parser.parse_args(argv)

    all_tags = (args.tags == 'all')
    res = defaultdict(list)

    if Path(args.file).is_file() and Path(args.output).is_dir():
        for e in tf.train.summary_iterator(args.file):
            for v in e.summary.value:
                if all_tags or (v.tag in args.tags):
                    res[v.tag].append(v.simple_value)

        for key, value in res.items():
            filename = "{}/{}{}".format(Path(args.output).absolute(),
                                        key.replace('/', '-'),
                                        '.dat')
            with open(filename, 'w') as output:
                for v in value:
                    output.write("%s\n" % v)


if __name__ == "__main__":
    main(sys.argv[1:])

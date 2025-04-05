#!/usr/bin/env python3
"""
Split multiple ABC files into single tune files.
"""

import argparse
import re
from dataclasses import dataclass

from abctools.utils import get_target_file, title_parser


NEW_TUNE = re.compile(r'([xX]:\s?\d+)')
TITLE = re.compile(r'[Tt]:\s*(.*)')


@dataclass
class TuneData():
    title: str
    tune: str
    header: str


def split(target):
    """Handles file io, passes to _spilt for content handling.
    """
    input_text = target.read_text()
    output = _split(input_text)
    if len(output) < 2:
        print(f'[INFO] File {target} contained 1 or fewer tunes')
        return
    for tune in output:
        (target.parent / (tune.title + '.abc')).write_text(('\n'.join(tune.header) + tune.tune))


def _split(text):
    splits = NEW_TUNE.split(text)
    header = []
    first_tune_found = False
    tunes = []
    for i, split in enumerate(splits):
        if NEW_TUNE.match(split):
            first_tune_found = True
            tune = TuneData(
                title=TITLE.findall(splits[i+1])[0],
                tune=split + splits[i + 1],
                header=header
            )
            tunes.append(tune)

        if not first_tune_found:
            header.append(split)
    return tunes


def get_opts():
    """Argparser details"""
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument(
        'target',
        help="Which folder to operate upon.",
    )
    opts = parser.parse_args()
    return opts


def main():
    opts = get_opts()
    targets = get_target_file(opts.target)
    for target in targets:
        split(target)


if __name__ == '__main__':
    main()

"""
.. include:: ../README.md
.. include:: ../docs/requirements.md
"""

import os, sys

from spamdetector.files import get_files_from_dir
from spamdetector.analyzer.data_structures import MailAnalyzer
from spamdetector.display import print_output


def _app(file: str, wordlist, add_headers: bool, verbose: bool, output_format: str) -> None:
    wordlist = wordlist.read().splitlines()
    data = []

    analyzer = MailAnalyzer(wordlist)

    if os.path.isdir(file):
        file_list = get_files_from_dir(file)
        for mail_path in file_list:
            analysis = analyzer.analyze(mail_path, add_headers)
            data.append(analysis)

    elif os.path.isfile(file):
        analysis = analyzer.analyze(file, add_headers)
        data.append(analysis)

    else:
        print('The file or directory doesn\'t exist')
        sys.exit(1)

    spam = 0
    warning = 0
    trust = 0

    print_output(data, output_format=output_format, verbose=verbose)

    for analysis in data:
        if analysis.is_spam() == 'Spam':
            spam += 1
        if analysis.is_spam() == 'Warning':
            warning += 1
        if analysis.is_spam() == 'Trust':
            trust += 1

    print('Spam: ', spam, 'su', len(data))
    print('Warning: ', warning, 'su', len(data))
    print('Trust: ', trust, 'su', len(data))

#!/usr/bin/env python3

import argparse
import re
import sys
import urllib.parse
import urllib.request
from collections import OrderedDict


def set_proxy(proxy):
    proxy_support = urllib.request.ProxyHandler({'https': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)


def bibformat(original_data):
    import bibtexparser
    from bibtexparser.bparser import BibTexParser
    from bibtexparser.bwriter import BibTexWriter
    parser = BibTexParser(common_strings=True)
    parser.homogenize_fields = True
    parser.ignore_nonstandard_types = False
    bib = bibtexparser.loads(original_data, parser)
    writer = BibTexWriter()
    writer.indent = '\t'
    return bibtexparser.dumps(bib, writer).strip()


def convert(doi):
    req = urllib.request.Request(
        url='https://doi.org/{}'.format(doi),
        headers={'Accept': 'application/x-bibtex'}
    )
    with urllib.request.urlopen(req) as response:
        lines = bibformat(response.read().decode()).splitlines()

    type = lines[0].split('{')[0][1:]

    tags = OrderedDict()
    for line in lines:
        match = re.search('^\t(.*?) = {(.*?)},?$', line)
        if not match:
            match = re.search('^\t(.*?) = (.*?),?$', line)
        if match:
            tags[match.group(1)] = match.group(2)

    if 'url' in tags.keys():
        del tags['url']

    id = ''
    if 'author' in tags.keys():
        first_author = tags['author'].split(' and ')[0]
        last_name = first_author.split(' ')[-1]
        id = id + ''.join([c.lower() for c in last_name if c.isalpha()])
    elif 'editor' in tags.keys():
        # example DOI: 10.2514/1.g002745
        first_editor = tags['editor'].split(' and ')[0]
        last_name = first_editor.split(' ')[-1]
        id = id + ''.join([c.lower() for c in last_name if c.isalpha()])
    else:
        # example DOI: 10.1007/978-0-387-40065-5
        id = id + 'na'
    if 'year' in tags.keys():
        id = id + tags['year']
    else:
        id = id + '0000'
    if 'title' in tags.keys():
        first_word = tags['title'].split(' ')[0]
        id = id + ''.join([c.lower() for c in first_word if c.isalpha()])
    else:
        id = id + 'na'

    val = ''
    val = val + '@' + type + '{' + id
    for key in tags.keys():
        val = val + ',\n' + '  ' + key + ' = {' + tags[key] + '}'
    val = val + '\n}'
    return val


def main():
    parser = argparse.ArgumentParser(description='Generate BibTeX from DOI.')
    parser.add_argument('-i', action='store_true', help='run interactively')
    parser.add_argument('-x', '--proxy', help='set HTTP proxy')
    parser.add_argument('DOI', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if args.proxy:
        set_proxy(args.proxy)

    is_first = True

    for doi in args.DOI:
        if is_first:
            is_first = False
            print(convert(doi))
        else:
            print('\n' + convert(doi))

    if args.i:
        for line in sys.stdin:
            doi = line.strip()
            if doi:
                if is_first:
                    is_first = False
                    print(convert(doi))
                else:
                    print('\n' + convert(doi))


if __name__ == '__main__':
    main()

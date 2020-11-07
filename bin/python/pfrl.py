#! /usr/bin/python3

# Should implement this in lua instead
# From https://stackoverflow.com/questions/40993488/convert-markdown-links-to-html-with-pandoc

import panflute as pf
import sys

def action(elem, doc):
    if isinstance(elem, pf.Link) and ".md" in elem.url:
        print(elem.url, file=sys.stderr, end = " --> ")
        if elem.url.endswith('.md'):
            elem.url = elem.url[:-3] + '.pdf'
        elem.url = elem.url.replace(".md#", ".pdf#")
        print(elem.url, file=sys.stderr)
        return elem

if __name__ == '__main__':
    pf.run_filter(action)

# Should implement this in lua instead
# From https://stackoverflow.com/questions/40993488/convert-markdown-links-to-html-with-pandoc

import panflute as pf

def action (elem, doc):
    if isinstance(elem, pf.Link) and elem.url.endswith('.md'):
        elem.url = elem.url[:-3] + '.pdf'
        return elem

if __name__ == '__main__':
    pf.run_filter(action)

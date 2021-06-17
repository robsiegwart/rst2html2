"""
rst-wrapper

Provides a command-line-interface to the native Docutils conversion utility
for converting reStructuredText to HTML, with support for CSS theme selection.

Usage ::

    rst2 INPUT_FILE OUTPUT_FILE --style=STYLENAME

Arguments to the ``--style`` option include:

- 
- 
- 

"""
import os
import click
from docutils.core import publish_file
from bs4 import BeautifulSoup as Soup


local_dir = os.path.dirname(__file__)


def html_suffix(string):
    """Replace or add an html extension to a filename string."""
    e = string.split('.')
    return '.'.join(e[:-1]) + '.html' if len(e) > 1 else e[0] + '.html'


STYLES = {
    'classless':    'classless.css',
    'latex':        'latex.min.css',
    'bamboo':       'bamboo.min.css',
    'tufte':        'tufte.css'
}


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output_file', default=None, help='Name of output file. Defaults to <input_file>.html.')
@click.option('-s', '--style', default=None, help='Style name for output HTML.',
                type=click.Choice(STYLES.keys()))
def convert(input_file, output_file, style):
    """Convert a reStructuredText file to HTML"""
    output_file = output_file if output_file else html_suffix(input_file)

    html = publish_file(
        source_path=input_file,
        destination_path=output_file,
        writer_name='html'
    )

    if style:
        css_file = STYLES[style]
        with open(os.path.join(local_dir, 'css', css_file)) as f:
            css_contents = f.read()
        
        soup = Soup(html, 'html.parser')
        head = soup.find('head')
        tag = soup.new_tag('style')
        tag.append(css_contents)
        head.append(tag)
        
        with open(output_file,'w') as f:
            f.write(soup.prettify())

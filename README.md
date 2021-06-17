# rst2html2

A wrapper for Docutils' conversion utility for converting reStructuredText files to HTML.
Creates a binary executable via `click` which can be called at the command line. Also
features some included CSS styles to style the published HTML.

## Install

After downloading, in your virtualenv, issue:

    pip install .


## Included CSS files

- [bamboo](https://github.com/rilwis/bamboo)
- [classless](https://github.com/emareg/classlesscss)
- [tufte](https://github.com/edwardtufte/et-book)

## Usage

    Usage: rst2html2 [OPTIONS] INPUT_FILE

    Convert a reStructuredText file to HTML

    Options:
    -o, --output_file TEXT          Name of output file. Defaults to
                                    <input_file>.html.
    -s, --style [classless|bamboo|tufte]
                                    Style name for output HTML. Defaults to
                                    none.
    --help                          Show this message and exit.
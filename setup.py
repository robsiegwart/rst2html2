from setuptools import setup

setup(
    name='rst2html2',
    author='Rob Siegwart',
    description='Wrapper utility to convert reStructuredText to HTML via Docutils with optional CSS',
    version='0.1.0',
    packages=['rst2html2'],
    install_requires=['click','docutils'],
    entry_points='''
        [console_scripts]
        rst2html2=rst2html2:convert
    '''
)
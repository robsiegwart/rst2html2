from setuptools import setup

setup(
    name='rst2html2',
    author='Rob Siegwart',
    description='Wrapper utility to convert reStructuredText to HTML via Docutils',
    version=0.1,
    packages=['rst2html2'],
    install_requires=['click','docutils'],
    # include_package_data=True,
    entry_points='''
        [console_scripts]
        rst2=rst2:convert
    '''
)
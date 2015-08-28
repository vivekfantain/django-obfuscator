from distutils.core import setup

desc = """
Used to obfuscate the sensitive information from database tables.
"""

setup(
    name='django-obfuscator',
    packages=['django-obfuscator'],
    version='0.1',
    description=desc,
    author='Vivek Venugopalan',
    author_email='vivek@fantain.com',
    url='https://github.com/vivekfantain/django-obfuscator',
    download_url='https://github.com/peterldowns/mypackage/tarball/0.1',
    keywords=['obfuscate', 'django-obfuscate'],
    classifiers=[],
)

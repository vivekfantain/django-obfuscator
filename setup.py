from distutils.core import setup


desc = """ Obfuscate sensitive information in production django databases so
that it can be distributed to various developers."""

setup(
    name='django-obfuscator',
    packages=['django-obfuscator'],
    version='0.1',
    description=desc,
    author='Vivek Venugopalan',
    author_email='vivek@fantain.com',
    url='https://github.com/vivekfantain/django-obfuscator',
    download_url='https://github.com/vivekfantain/django-obfuscator/tarball/0.1',
    keywords=['obfuscate', 'django-obfuscate'],
    classifiers=[],
)

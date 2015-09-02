"""
Copyright  2015, Fantain Sports Private Limited

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from setuptools import setup

desc = """ Obfuscate sensitive information in production django databases so
that it can be distributed to various developers."""

setup(
    name='django_obfuscator',
    packages=['data_obfuscator'],
    version='0.8',

    include_package_data=True,

    description=desc,
    author='Vivek Venugopalan',
    author_email='vivek@fantain.com',
    license='Apache License 2.0',
    url='https://github.com/vivekfantain/django-obfuscator',
    download_url='https://github.com/vivekfantain/django-obfuscator/tarball/0.1',
    keywords=['obfuscate', 'django-obfuscate'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

)


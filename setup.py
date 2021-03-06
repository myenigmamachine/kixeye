import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='support',
        version='1.0',
        packages=['support', 'kixeye'],
        include_package_data=True,
        license='BSD License',
        description='A simple customer support system for a fictional online game.',
        long_description=README,
        url='https://localhost:8000/',
        author='Danny Key',
        author_email='danny.key.88@gmail.com',
        classifiers=[
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: BSD License',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python',
                    # Replace these appropriately if you are stuck on Python 2.
                    'Programming Language :: Python :: 2.6',
                    'Topic :: Internet :: WWW/HTTPS',
                    'Topic :: Internet :: WWW/HTTPS :: Dynamic Content',
                ],
    )

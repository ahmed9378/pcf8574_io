from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Operating System :: Other OS',
    'Topic :: System :: Hardware :: Hardware Drivers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pcf8574_io',
    version='0.0.2',
    description='setup pin mode and read, write to PCF8574 pins',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Ahmed Omar',
    author_email='ahmed.bm78@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='PCF8574',
    packages=find_packages(),
    install_requires=['smbus2']
)
from setuptools import setup

setup(
    name='queue-utils',
    version='0.12.0',
    author='Mighty Mouse',
    author_email='mm@mighty-mouse.com',
    packages=[
        'queue_utils'
    ],
    scripts=[
    ],
    url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE.txt',
    description='queue-utils encapsulates rabbitMQ',
    long_description='queue-utils encapsulates rabbitMQ',
    install_requires=[
        "pika"
    ],
)

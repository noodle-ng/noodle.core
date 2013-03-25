from setuptools import setup, find_packages

setup(
    name='noodle.core',
    version='0.1',
    author='',
    author_email='',
    url='https://github.com/noodle-ng/noodle.core/',
    license='',
    description='Noodle NG Core Components',
    long_description=open('README.md').read(),
    install_requires=[
        'SQLAlchemy'
        ],
    packages=find_packages(exclude=['tests']),
    namespace_packages=['noodle'],
)
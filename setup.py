from setuptools import setup

setup(
    name='calculator',
    packages=['calculator'],
    include_package_data=True,
    install_requires=[
        'flask','Flask-Pydantic'
    ],
)
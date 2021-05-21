from setuptools import setup

setup(
    name='drutils',
    version='.1',
    packages=['pdutils'],
    url='',
    license='MIT',
    author='Dan Ross',
    author_email='dan@rosspixelworks.com',
    description='Dan\'s Utilities',
    required=[
        "pandas>=1.2"
    ],
    extras={
        "tests": [
            "pytest"
        ]
    }

)

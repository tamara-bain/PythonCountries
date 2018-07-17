"""
Countries
-------------
Country to Country Code Python Mapping
"""

from setuptools import setup

setup(
    name='Python Countries',
    version='0.1',
    url='https://github.com/tamara-bain/PythonCountries',
    license='MIT',
    description='Python Countries',

    py_modules=['countries'],
    platforms='any',
    test_suite='[test_countries]',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)

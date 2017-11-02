from setuptools import find_packages, setup

dependencies = []

long_description = short_description = 'Table IO'

setup(
    name='wib',
    version='0.1.0',
    url='https://github.com/MatthewJA/bathurst',
    license='BSD',
    author='Matthew Alger',
    author_email='hello.i.am.matthewja@gmail.com',
    description=short_description,
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[],
    entry_points={
        'console_scripts': [],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

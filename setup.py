from setuptools import setup

setup(
    name='pytry_explorer',
    packages=['pytry_explorer'],
    install_requires=['pytry'],
    version='0.0.1',
    entry_points=dict(
        console_scripts=['pytry-explorer = pytry_explorer.explorer:run'],
        ),
    author='Terry Stewart',
    description='Exploring effects of parameter changes on pytry models',
    author_email='terry.stewart@gmail.com',
    url='https://github.com/tcstewar/pytry_explorer',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        ]
    )

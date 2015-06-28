from setuptools import setup, find_packages

setup(
    name="stats-aggregator",
    version="0.0.1",
    author="Mathieu Sabourin",
    author_email="mathieu.c.sabourin@gmail.com",
    license="lgpl",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Topic :: Scientific/Engineering",
        "Topic :: System :: Monitoring",
    ]
)

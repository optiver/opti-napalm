"""setup.py file."""
from setuptools import setup, find_packages

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

with open("README.md", "r") as fs:
    long_description = fs.read()


__author__ = "David Barroso <dbarrosop@dravetech.com>"

setup(
    name="opti-napalm",
    version="4.0.1",
    packages=find_packages(exclude=("test*",)),
    test_suite="test_base",
    author="David Barroso, Kirk Byers, Mircea Ulinic",
    author_email="dbarrosop@dravetech.com, ping@mirceaulinic.net, ktbyers@twb-tech.com, ams_pypi@optiver.com",
    description="Optiver's fork of NAPALM",
    license="Apache 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    url="https://github.com/optiver/opti-napalm",
    include_package_data=True,
    install_requires=reqs,
    entry_points={
        "console_scripts": [
            "cl_napalm_configure=napalm.base.clitools.cl_napalm_configure:main",
            "cl_napalm_test=napalm.base.clitools.cl_napalm_test:main",
            "cl_napalm_validate=napalm.base.clitools.cl_napalm_validate:main",
            "napalm=napalm.base.clitools.cl_napalm:main",
        ]
    },
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="indego",
    version="1.1.0",
    author="Eric O'Callaghan",
    author_email="eric@ericoc.com",
    description="Python3 library for working with the Philadelphia Indego Bike Share API",
    long_description=long_description,
    keywords="philadelphia philly indego rideindego bicycle bike share bikeshare bike-share api",
    long_description_content_type="text/markdown",
    url="https://github.com/ericoc/indego-py-lib/",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Indego Philly Bike Share": "https://www.rideindego.com/",
        "Project maintainer": "https://ericoc.com/"
    }
)

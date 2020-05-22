"""
Setup, test, build, package, and install apt_scraper package.
Author: Matt Bucter
"""
from setuptools import find_packages, setup


_VER = "0.1.0"

setup(
    name="apt-scraper",
    url="https://github.com/mbucter/apt-scraper",
    version=_VER,
    description="Scrape apartment prices.",
    author="Matt Bucter",
    author_email="matthewbucter@gmail.com",
    packages=find_packages(exclude=["test_.*", "tests"]),
    include_package_data=True,
    install_requires=[
        "click",
        "pandas >= 1.0.3",
        "bs4",
        "requests",
    ],
    entry_points={"console_scripts": ["apt-scraper=apt_scraper.extract:extract"]}
)

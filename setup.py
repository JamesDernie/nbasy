import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbasy",
    version="0.0.1",
    author="James Dernie",
    author_email="jamesdernie@gmail.com",
    description="Package for getting player, team and game stats from stats.nba.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JamesDernie/nbasy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
)
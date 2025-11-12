from setuptools import setup, find_packages

setup(
    name="json_toon_converter",  # Changed name here
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "toon-python",  # This is the dependency we'll need for converting TOON
    ],
    entry_points={
        "console_scripts": [
            "json-toon-converter=json_to_toon_converter.converter:main",  # CLI entry point updated
        ],
    },
    author="Oren Grinker",
    author_email="orengr4@gmail.com",
    description="A package to convert JSON to TOON and TOON to JSON",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/OrenGrinker/json-toon-converter",  # Update to your repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

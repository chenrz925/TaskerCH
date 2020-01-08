import taskerch as package

import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="TaskerCH",
    version=package.__version__,
    author="Runze Chen",
    author_email="chenrz925@icloud.com",
    description="A scalable and extendable experiment task scheduler.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chenrz925/TaskerCH",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7",
    install_requires=[
        "toml>=0.10.0"
    ]
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="archicad",
    version="25.3000",
    author="GRAPHISOFT SE",
    author_email="archicadapi@graphisoft.com",
    description="Python binding for the ARCHICAD JSON command interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://archicadapi.graphisoft.com/archicadPythonPackage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    license='Apache'
)

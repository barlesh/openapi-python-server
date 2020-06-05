import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my auto server",
    version="0.0.1",
    author="BarLesh",
    author_email="barlesh8@gmail.com",
    description="A skelaton of a python microservice with automation API creation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Barlesh/my-auto-flask-service",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
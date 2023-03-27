from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="macpip",
    version="0.0.1",
    author="mbranch",
    author_email="",
    license="MIT",
    description="A tool to output macOS apps in requirements format.",
    url="https://github.com/mubranch/mpip",
    py_modules=["macpip, 'app"],
    packages=find_namespace_packages(),
    install_requires=[requirements],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    entry_points="""
    [console_scripts]]
    macpip = macpip:cli""",
)

from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="mpip",
    version="0.0.1",
    author="mbranch",
    author_email="",
    license="MIT",
    description="A tool to output macOS apps in requirements format.",
    url="",
    py_modules=["mpip, 'app"],
    packages=find_namespace_packages(),
    install_requires=[requirements],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: MACOS",
    ],
    entry_points="""
    [console_scripts]]
    mpip = mpip:cli""",
)

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="a2jpg",
    version="0.0.1",
    author="tonyguo",
    author_email="tony92151@gmail.com",
    url="https://github.com/tony92151/a2jpg",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['a2jpg=a2jpg.a2jpg:main'],
    },
    python_requires=">=3.6",
)

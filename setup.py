from setuptools import setup, find_packages
import sys

requirements = [
    "Pillow>=9.0.0",
    "keyboard>=0.13.5",
    "mouse>=0.7.1",
    "pynput>=1.7.6",
]

if sys.platform == 'win32':
    requirements.append("pywin32>=305")

setup(
    name="myrecorder",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)

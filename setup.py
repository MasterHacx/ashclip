from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ashclip",
    version="1.1.0",
    author="MasterHacx",
    author_email="official.akash497@gmail.com",
    description="A discreet CLI tool to fetch file content from Nexus Hub to clipboard via hotkey (Ctrl+Shift+A).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MasterHacx/ashclip",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    install_requires=[
        "keyboard",
        "pyperclip",
        "requests",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ashclip=ashclip.main:main",
        ],
    },
)
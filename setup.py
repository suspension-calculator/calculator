from setuptools import setup, find_packages

setup(
    name="suspension-calculator",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "matplotlib",
        "pyinstaller",
        # tkinter is a built-in package, don't include it here
    ],
    python_requires=">=3.13",  # Specify minimum Python version
)
from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    url="https://github.com/eagle/ft_package",
    author="eagle",
    author_email="eagle@42.fr",
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)

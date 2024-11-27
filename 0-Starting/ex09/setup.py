from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="djanusz",
    author_email="djanusz@student.42.fr",
    url="https://github.com/SolDavid76",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
)

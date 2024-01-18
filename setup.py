from setuptools import setup, find_packages

setup(
    name="getent2",
    version="0.2",
    author="Wijnand Modderman-Lenstra",
    author_email="maze@pyth0n.org",
    description="Python interface to the POSIX getent family of commands",
    long_description=open("README.rst").read(),
    license="MIT",
    keywords="getent group passwd shadow network alias host",
    packages=["getent"],
)

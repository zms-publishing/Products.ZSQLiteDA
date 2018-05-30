from setuptools import setup, find_packages


version = "0.6.1"

setup(
    name="Products.ZSQLiteDA",
    version=version,
    description="SQLite database adapter for Zope2",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="SQLite",
    author="HOFFMANN+LIEBENBERG in association with SNTL Publishing, Hajime Nakagami",
    author_email="zms@sntl-publishing.com",
    url="https://github.com/nakagami/Products.ZSQLiteDA",
    license="ZPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["Products.ZSQLMethods>=3.0.2"],
)

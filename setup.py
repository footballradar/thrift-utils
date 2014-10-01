from distutils.core import setup


setup(
    name='thrift-utils',
    version='0.0.1',
    packages=['fr_thrift'],
    install_requires=[
        "thrift",
        "kazoo",
        "ipython",
    ],
)

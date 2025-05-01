from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="drunc_messages",
    package_data={
        'drunc_messages': []
    },
    install_requires=[
        "grpcio>=1.68.0",
        "grpcio-status>=1.68.0",
        "grpcio-tools>=1.68.0",
        "protobuf>=5.28.1",
    ],
    extras_require={"develop": [
        "ipdb",
        "ipython"
    ]},
)

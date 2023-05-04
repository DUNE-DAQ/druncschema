from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="druncschema",
    package_data={
        'druncschema': []
    },
    install_requires=[],
    extras_require={"develop": [
        "ipdb",
        "ipython"
    ]},
)

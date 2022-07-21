# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import setuptools

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def version_handler() -> str:
    version = 1,0,0
    version_str = ".".join(str(i) for i in version)

    with open("src/AthenaGuiLib/_info/_v.py", "w") as file:
        file.write(f"def _version():\n    return '{version_str}'")

    return version_str

setuptools.setup(
    name="AthenaGuiLib",
    version=version_handler(),
    author="Andreas Sas",
    author_email="",
    description="A Library of DearPyGui elements, to be used in Directive Athena projects",
    url="https://github.com/DirectiveAthena/AthenaGuiLib",
    project_urls={
        "Bug Tracker": "https://github.com/DirectiveAthena/AthenaGuiLib/issues",
    },
    license="GPLv3",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=[
        "DearPyGui>=1.6.2",
        "AthenaLib>=0.2.0",
        "AthenaColor>=5.1.0"
    ]
)
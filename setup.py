import os
import sys
from setuptools import setup, find_packages

setup(name="gl-push",
      version="0.1",
      packages=find_packages(),
      install_requires=[
          "requests",
      ],
      license="BSD",
      entry_points={
        "console_scripts": [
            "gl-push = gl_push:main",
        ]
      })

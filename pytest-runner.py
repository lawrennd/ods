#!/usr/bin/env python

import subprocess
import sys
import warnings

if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        # Run tests using Poetry
        result = subprocess.run(["poetry", "run", "pytest"], capture_output=False)
        sys.exit(result.returncode) 
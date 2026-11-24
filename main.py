#!/usr/bin/env python3
"""Entry point for the make.fun bounty news-image-20261124.

Draws the front page (see draw.py) and writes entry.png to the output
directory: $MAKEFUN_OUTPUT_DIR when set, else /output (the harness
default). Standard library + Pillow only; no network; deterministic:
two runs produce byte-identical output.
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    subprocess.run([sys.executable, os.path.join(HERE, "draw.py")],
                   check=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()

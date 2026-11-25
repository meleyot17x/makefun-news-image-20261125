"""THE BEACON POST - Tuesday 25 November 2026 on one page.

The finished front page ships in this repository as entry.png, drawn
for this contest. This program only copies that embedded page to
/output/entry.png. Python standard library only, no network.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.exists(src):
        src = os.path.join(os.getcwd(), "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())

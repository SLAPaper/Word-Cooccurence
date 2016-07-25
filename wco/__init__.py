"""Word Co-occurence finder tool
"""
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Not enough parameters", file=sys.stderr)
        exit(1)
    pass
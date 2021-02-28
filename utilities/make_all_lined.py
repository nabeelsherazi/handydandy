import time
import os
from ..misc.decorators import timeit

"""
By Nabeel Sherazi, sherazi.n@husky.neu.edu
Batch file program that creates line numbered versions of all text files in
current directory (but not any subdirectories). Place script in directory
and run to create files. Wait for "Done" in console window to indicate finish.
"""


@timeit
def create_lined_ver(filename):
    """ Creates a new version of filename with line numbers added and outputs
    it as filename_lined.txt. """
    with open(filename + ".txt", "r") as f_in, open(filename + "_lined" + ".txt", "w") as f_out:
        for (num, line) in enumerate(f_in):
            f_out.write("[{}]: {}".format(num, line))


if __name__ == "__main__":
    fnames = []
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        for f in filenames:
            if f.endswith(".txt"):
                fnames.append(f)
        break  # Look only in this directory, not any subdirectories.
    print("Found", len(fnames), "files to convert.")
    for f in fnames:
        f = f[:-4]
        create_lined_ver(f)
    print("Done.")
    input()

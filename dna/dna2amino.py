import time
import os

"""
By Nabeel Sherazi, sherazi.n@husky.neu.edu

Batch file program that takes an input DNA strand and converts it to its
corresponding set of amino acid pairs. Input strands must be 3 to 5 and
non-coding. Place the input strand in the file "input_DNA.txt" and the
program will write to file "output_amino.txt."
Example:

Input: 3' TAC CAA ACT 5'
RNA Transcription: 5' AUG GUU UGA 3'
Output: MET-VAL-STOP
"""

RNA = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C', ' ': ' ', "\n": "\n", "3": "5'", "5'": "3'"}

#  So this is wrong :)
gencode = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
    'ACA': 'U', 'ACC': 'U', 'ACG': 'U', 'ACU': 'U',
    'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
    'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
    'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W',
    "3' ": "", "5' ": "", "\n": "\n", '': ''}


def timeit(func):
    """ Function decorator to print run time in console window. """
    def wrapper(*arg, **kwargs):
        t0 = time.clock()
        func(*arg, **kwargs)
        t1 = time.clock()
        print("Completed in {0:.2f} seconds.".format(t1 - t0))
    return wrapper


def prep_strand(strand):
    strand = strand.strip("35'")
    strand = strand.replace(" ", '')
    strand = strand.upper()
    return strand


def transcribe(strand):
    """ Translates a given DNA strand string into an RNA strand. """
    result = ''
    for c in strand:
        converted = RNA[c]
        if converted == -1:
            converted = "[ERR]"
        result += converted
    return result


def convert_amino(strand):
    result = ''
    for i in range(0, len(strand) - 3):
        converted = gencode[strand[(3 * i):(3 * i + 3)]]
        if converted == -1:
            converted = "[ERR]"
        result += converted
    return result


print("Input must be in the form of a 3 to 5 strand. Enter strands according to\nFASTA syntax. 3' or 5' markers, or spaces, may be present, but will be \nremoved.\n")
input("Press enter when input file is ready for conversion. If input file is \nnot present, press enter and one will be created for you.\n")

try:
    with open("input_DNA.txt", "r") as f_in:
        pass
except FileNotFoundError:
    with open("input_DNA.txt", "r+") as f_in:
        pass
    print("Input file not found - creating one. Please add DNA code in 3 to 5 syntax and rerun.")
    input()
    raise SystemExit
else:
    with open("input_DNA.txt", "r") as f_in, open("output_amino.txt", "w+") as f_out:
        data = f_in.readlines()
        for (ix, strand) in enumerate(data):
            data[ix] = prep_strand(strand)
            data[ix] = transcribe(strand)
        f_out.write("TRANSCRIBED RNA:")
        f_out.write("\n\n")
        for line in data:
            f_out.write(line)
        f_out.write("\n\n")
        f_out.write("AMINO ACIDS:")
        f_out.write("\n\n")
        for line in data:
            f_out.write(convert_amino(line))
    print("Done.")
    input()

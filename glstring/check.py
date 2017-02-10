#!/usr/bin/env python3
"""
check.py

Functions to do a few sanity checks of a GL String

Checks the following...
- if a locus is found in more than one locus block
  e.g., this is good
  HLA-A*01:01/HLA-A*01:02+HLA-A*24:02^HLA-B*08:01+HLA-B*44:02^"
  e.g., this is bad
  HLA-A*01:01/HLA-A*01:02+HLA-A*24:02^HLA-B*08:01+HLA-A*44:02^"

- if any of the following contain more than one locus
  genotype lists
  genotypes
  allele lists

Note: Both genotypes and genotype lists may contain phased loci,
      and so these may contain multiple loci
"""


from .glstring import get_loci
from .glstring import get_allele_lists
from .glstring import get_genotypes
from .glstring import get_genotype_lists


def get_duplicates(setlist):
    """
    Takes a list of sets, and returns a set of items that are found in
    more than one set in the list
    """
    duplicates = set()
    for i, myset in enumerate(setlist):
        othersets = set().union(*setlist[i+1:])
        duplicates.update(myset & othersets)
    return duplicates


def locus_blocks(glstring):
    """
    Takes a GL String and checks to see if any loci are found in
    more than one locus block.
    Returns a tuple containing a list of locus blocks, and set of loci
    found in more than one block
    """
    locusblocks = glstring.split('^')
    duplicates = set()
    if len(locusblocks) > 1:
        loci = []
        for locusblock in locusblocks:
            loci.append(get_loci(locusblock))
        duplicates = get_duplicates(loci)
    return locusblocks, duplicates


def genotype_lists(glstring):
    """
    Takes a GL String, and checks to see if any unphased genotype lists
    contain more than one locus. A list of tuples is returned. Each
    tuple consists of the genotype list, a set of loci found in the
    genotype list, and a text string. For genotype lists containing of
    only unphased genotypes, the text string is either 'OK' (if only one
    locus is found), or 'WARNING' (if more than one locus if found).
    For for genotype lists that contain at lease one phased genotype
    (containing '~'), the text string is 'Phased - check separately'
    """
    genotype_lists = get_genotype_lists(glstring)
    checked_gl = []
    for genotype_list in genotype_lists:
        loci = get_loci(genotype_list)
        if len(loci) > 1:
            if '~' not in genotype_list:
                msg = 'WARNING'
            else:
                msg = 'Phased, check separately'
        else:
            msg = 'OK'
        checked_gl.append((genotype_list, loci, msg))
    return checked_gl


def allele_lists(glstring):
    """
    Takes a GL String, and checks to see if there are more than one
    locus in any of the allele lists. A list of tuples is returned. Each
    tuple consists of the allele list, a set of loci found in the allele
    list, and a text string. The text string is either 'OK' (if only one
    locus is found), or 'WARNING' (if more than one locus if found).
    """
    allele_lists = get_allele_lists(glstring)
    checked_al = []
    if len(allele_lists) > 0:
        for allele_list in allele_lists:
            loci = get_loci(allele_list)
            if len(loci) > 1:
                msg = 'WARNING'
            else:
                msg = 'OK'
            checked_al.append((allele_list, loci, msg))
    return checked_al


def genotypes(glstring):
    """
    Takes a GL String, and checks to see if any unphased genotypes
    contain more than one locus. A list of tuples is returned. Each
    tuple consists of the genotype, a set of loci found in the genotype,
    and a text string. For unphased genotypes, the text string is either
    'OK' (if only one locus is found), or 'WARNING' (if more than one
    locus if found). For phased genotypes (containing '~'), the text
    string is 'Phased - check separately'
    """
    genotypes = get_genotypes(glstring)
    checked_gt = []
    for genotype in genotypes:
        loci = get_loci(genotype)
        if len(loci) > 1:
            if '~' in genotype:
                msg = 'Phased - Check separately'
            else:
                msg = 'Unphased - WARNING'
        else:
            msg = 'OK'
        checked_gt.append((genotype, loci, msg))
    return checked_gt


def printchecked(checked, desc):
    """
    Takes a list of checked items and a description, and prints them.
    """
    print('Checking ' + desc, '...')
    if len(checked) > 0:
        for item in checked:
            print(item)
    else:
        print('No ' + desc + ' found')
    print()


def main():
    testgl = [
        # good
        # "HLA-A*01:01+HLA-A*24:02^HLA-B*44:01+HLA-B*44:02",
        # "HLA-A*01:01+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03",
        # "HLA-A*01:01+HLA-A*01:02",
        # "HLA-A*01:01/HLA-A*01:02",
        # "HLA-A*01:01/HLA-A*01:02+HLA-A*24:02",
        # ("HLA-A*01:01/HLA-A*01:02+HLA-A*24:02|"
        #  "HLA-A*01:03/HLA-A*01:04+HLA-A*24:03"),
        # "HLA-A*01:01~HLA-B*44:02+HLA-A*02:01~HLA-B*08:01",
        # "HLA-A*01:01+HLA-A*24:02^HLA-B*08:01+HLA-B*44:02",
        ("HLA-A*01:01/HLA-A*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03^"
            "HLA-B*08:01+HLA-B*44:01/HLA-B*44:02^"
            "HLA-C*01:02+HLA-C*01:03^"
            "HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92"),
        # bad
        # "HLA-A*01:01+HLA-A*24:02^HLA-A*01:03+HLA-A*24:03",
        # "HLA-A*01:01+HLA-A*24:02|HLA-B*44:01+HLA-B*44:02",
        # "HLA-A*01:01+HLA-B*01:02",
        # "HLA-B*44:01/HLA-C*44:02",
        # ("HLA-A*01:01/HLA-A*01:02+HLA-A*24:02|"
        #  "HLA-A*01:03/HLA-A*01:04+HLA-B*24:03"),
        # ("HLA-A*01:01/HLA-A*01:02+HLA-A*24:02^HLA-B*08:01+HLA-B*44:02^"
        #  "HLA-A*01:01+HLA-A*24:02^HLA-B*08:01+HLA-B*44:02/HLA-A*01:01"),
        # ("HLA-A*01:01/HLA-A*01:02+HLA-A*24:02/HLA-B*08:01^"
        #  "HLA-C*01:02"),
        # ("HLA-A*01:01/HLA-A*01:02+HLA-A*24:02/HLA-B*08:01^"
        #  "HLA-C*01:02+HLA-A*01:01^"
        #  "HLA-DRB5*01:01~HLA-DRB1*03:01"),
        ("HLA-A*01:01/HLA-B*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03^"
            "HLA-B*08:01+HLA-B*44:01/HLA-B*44:02^"
            "HLA-C*01:02+HLA-A*01:01~HLA-C*01:03^"
            "HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92"),
    ]

    for gl in testgl:
        print("gl =", gl, "\n")

        print("Checking locus blocks...")
        locusblocks, duplicates = locus_blocks(gl)
        for locusblock in locusblocks:
            print(locusblock)
        if len(locusblocks) > 1:
            if len(duplicates) == 0:
                print("OK: no loci found in more than one locus block")
            else:
                if len(duplicates) == 1:
                    print("WARNING: Locus found in more than 1 locus block:",
                          duplicates)
                else:
                    print("WARNING: Loci found in more than 1 locus block:",
                          duplicates)
        else:
            print("Nothing to check: Only one locus block")
        print()

        printchecked(genotype_lists(gl), 'genotype lists')
        printchecked(genotypes(gl), 'genotypes')
        printchecked(allele_lists(gl), 'allele lists')

        if len(testgl) > 1:
            print("--------\n")


if __name__ == '__main__':
    main()

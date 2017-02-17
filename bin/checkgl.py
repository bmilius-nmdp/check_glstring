#!/usr/bin/env python3
"""
check_glstring.py

This script does a few sanity checks of a GL String

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

import argparse
import glstring.check as check


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--glstring",
                        required=True,
                        help="GL String to be checked",
                        type=str)
    args = parser.parse_args()

    if args.glstring:
        gl = args.glstring

    # print("\n", "GL String =", gl, "\n")

    print("\nChecking locus blocks...")
    locusblocks, duplicates = check.locus_blocks(gl)
    for locusblock in locusblocks:
        print("# ", locusblock,)
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

    check.printchecked(check.genotype_lists(gl), 'genotype lists')
    check.printchecked(check.genotypes(gl), 'genotypes')
    check.printchecked(check.allele_lists(gl), 'allele lists')


if __name__ == '__main__':
    main()

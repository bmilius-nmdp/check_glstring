#!/usr/bin/env python3
"""
glstring.py

functions for getting loci, alleles, allele lists, genotypes, genotype lists
and locus blocks from a GL String

also contains class for GlString with methods to do the above.
"""

import re


class GlString:
    """
    common base class for GL Strings
    """

    def __init__(self, gl, imgthla):
        self.gl = gl
        self.imgthla = imgthla

    def loci(self):
        """
        Takes GL String and returns a set containing all the loci
        """
        alleles = get_alleles(self.gl)
        loci = set()
        for allele in alleles:
            loci.add(allele.split('*')[0])
        return loci

    def alleles(self):
        """
        Takes a GL String, and returns a set containing all the alleles
        """
        alleles = set()
        for allele in re.split(r'[/~+|^]', self.gl):
            alleles.add(allele)
        return alleles

    def allele_lists(self):
        """
        Takes a GL String and returns a list of allele lists it contains
        """
        allele_lists = []
        for allele_list in re.split(r'[~+|^]', self.gl):
            if "/" in allele_list:
                allele_lists.append(allele_list)
        return allele_lists

    def genotypes(self):
        """
        Take a GL String, and return a list of genotypes
        """
        parsed = re.split(r'[|^]', self.gl)
        genotypes = []
        for genotype in parsed:
            if "+" in genotype:
                genotypes.append(genotype)
        return genotypes

    def genotype_lists(self):
        """
        Take a GL String, and return a list of genotype lists
        """
        parsed = re.split(r'[\^]', self.gl)
        genotype_lists = []
        for genotype_list in parsed:
            if "|" in genotype_list:
                genotype_lists.append(genotype_list)
        return genotype_lists

    def locus_blocks(self):
        """
        Take a GL String, and return a list of locus blocks
        """
        # return re.split(r'[\^]', glstring)
        return self.gl.split('^')


def get_loci(glstring):
    """
    Takes GL String and returns a set containing all the loci
    """
    alleles = get_alleles(glstring)
    loci = set()
    for allele in alleles:
        loci.add(allele.split('*')[0])
    return loci


def get_alleles(glstring):
    """
    Takes a GL String, and returns a set containing all the alleles
    """
    alleles = set()
    for allele in re.split(r'[/~+|^]', glstring):
        alleles.add(allele)
    return alleles


def get_allele_lists(glstring):
    """
    Takes a GL String and returns a list of allele lists it contains
    """
    allele_lists = []
    for allele_list in re.split(r'[~+|^]', glstring):
        if "/" in allele_list:
            allele_lists.append(allele_list)
    return allele_lists


def get_genotypes(glstring):
    """
    Take a GL String, and return a list of genotypes
    """
    parsed = re.split(r'[|^]', glstring)
    genotypes = []
    for genotype in parsed:
        if "+" in genotype:
            genotypes.append(genotype)
    return genotypes


def get_genotype_lists(glstring):
    """
    Take a GL String, and return a list of genotype lists
    """
    parsed = re.split(r'[\^]', glstring)
    genotype_lists = []
    for genotype_list in parsed:
        if "|" in genotype_list:
            genotype_lists.append(genotype_list)
    return genotype_lists


def get_locus_blocks(glstring):
    """
    Take a GL String, and return a list of locus blocks
    """
    # return re.split(r'[\^]', glstring)
    return glstring.split('^')


def main():
    pass


if __name__ == '__main__':
    main()

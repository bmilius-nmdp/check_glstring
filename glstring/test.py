#!/usr/bin/env python3

import re


class GlString:
    """
    returns lists of GlString objects (except alleles() which returns a set)
    """

    def __init__(self, gls, ver):
        self.gls = gls
        self.ver = ver

    def genotypes(self):
        """
        Take a GL String, and return a list of genotypes
        """
        parsed = re.split(r'[|^]', self.gls)
        genotypes = []
        for genotype in parsed:
            if "+" in genotype:
                gl = GlString(genotype, self.ver)
                genotypes.append(gl)
        return genotypes

    def allele_lists(self):
        """
        Takes a GL String and returns a list of allele lists it contains
        """
        allele_lists = []
        for allele_list in re.split(r'[~+|^]', self.gls):
            if "/" in allele_list:
                gl = GlString(allele_list, self.ver)
                allele_lists.append(gl)
        return allele_lists

    def alleles(self):
        """
        Takes a GL String, and returns a set containing all the alleles
        """
        alleles = set()
        for allele in re.split(r'[/~+|^]', self.gls):
            alleles.add(allele)
        return allele

    def __repr__(self):
        return('Test("{}", "{}")'.format(self.gls, self.ver))

    def __str__(self):
        return(self.gls)

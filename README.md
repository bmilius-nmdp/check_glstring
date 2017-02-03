# check_glstring.py

## Does a sanity check of a GL String

## checks...
* if locus found in more than one locus block
  *  e.g., this is good:
    * `HLA-A*01:01/HLA-A*01:02+HLA-A*24:02|HLA-A*01:03/HLA-A*01:04+HLA-A*24:03`
  * but, this is bad:
    * `HLA-A*01:01/HLA-A*01:02+HLA-A*24:02^HLA-A*01:03/HLA-A*01:04+HLA-A*24:03`

*  if a allele list contains more than one locus
  * e.g., this is good:
    * `HLA-B*44:01/HLA-B*44:02`
  * but, this is bad:
    * `HLA-B*44:01/HLA-C*44:02`

## todo:
    check_genotypelist
    check_genotype
    check_phased

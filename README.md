# check_glstring.py

## Does a sanity check of a GL String

## checks...
* if any locus is found in more than one locus block
    * good: `HLA-A*01:01+HLA-A*24:02^HLA-B*44:01+HLA-B*44:02`
    * bad:  `HLA-A*01:01+HLA-A*24:02^HLA-A*01:03+HLA-A*24:03`

* if any of the following contains more than one locus
  * genotype list
    * good: `HLA-A*01:01+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03`
    * bad:  `HLA-A*01:01+HLA-A*24:02|HLA-B*44:01+HLA-B*44:02`
  * genotype
    * good:  `HLA-A*01:01+HLA-A*01:02`
    * bad:   `HLA-A*01:01+HLA-B*01:02`
  * allele list
    * good: `HLA-B*44:01/HLA-B*44:02`
    * but:  `HLA-B*44:01/HLA-C*44:02`


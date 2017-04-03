pyglstring
----------

* Contains a python package with a module for handling GL Strings, and another for carrying out sanity checks on the string.

 - glstring.glstring
 - glstring.check

* Three scripts are included.

 * ``checkgl.py`` - imports the glstring package. You'll need to install the package by running ``pip install .`` from the top of distribution (where the setup.py file is located)

 * ``checkgl_standalone.py`` - all necessary function are included

 * ``checkgl_standaloneDR.py`` - same as above, but added special warning if genotype has differnt loci, but both are DR. 

* Each of the scripts does a sanity check of a GL String. These check...
  
 * if any locus is found in more than one locus block

  * good: ``HLA-A*01:01+HLA-A*24:02^HLA-A*01:03+HLA-A*24:03``
  * bad: ``HLA-A*01:01+HLA-A*24:02^HLA-B*44:01+HLA-B*44:02``

 * if any of the following contains more than one locus

  * genotype list

   * good: ``HLA-A*01:01+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03``
   * bad: ``HLA-A*01:01+HLA-A*24:02|HLA-B*44:01+HLA-B*44:02``

  * genotype

   * good: ``HLA-A*01:01+HLA-A*01:02``
   * bad: ``HLA-A*01:01+HLA-B*01:02``

  * allele list

   * good: ``HLA-B*44:01/HLA-B*44:02``
   * but:  ``HLA-B*44:01/HLA-C*44:02``

usage
-----
.. code::

    $ ./checkgl.py --help
    usage: checkgl.py [-h] -g GLSTRING

    optional arguments:
      -h, --help            show this help message and exit
      -g GLSTRING, --glstring GLSTRING
                            GL String to be checked

example with a sane GL String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    $ ./checkgl.py -g 'HLA-A*01:01/HLA-A*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03^HLA-B*08:01+HLA-B*44:01/HLA-B*44:02^HLA-C*01:02+HLA-C*01:03^HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92'

    GL String = HLA-A*01:01/HLA-A*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03^HLA-B*08:01+HLA-B*44:01/HLA-B*44:02^HLA-C*01:02+HLA-C*01:03^HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92

    Checking locus blocks...
    HLA-A*01:01/HLA-A*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03
    HLA-B*08:01+HLA-B*44:01/HLA-B*44:02
    HLA-C*01:02+HLA-C*01:03
    HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92
    OK: no loci found in more than one locus block

    Checking genotype lists ...
    ('HLA-A*01:01/HLA-A*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03', {'HLA-A'}, 'OK')

    Checking genotypes ...
    ('HLA-A*01:01/HLA-A*01:02+HLA-A*24:02', {'HLA-A'}, 'OK')
    ('HLA-A*01:03+HLA-A*24:03', {'HLA-A'}, 'OK')
    ('HLA-B*08:01+HLA-B*44:01/HLA-B*44:02', {'HLA-B'}, 'OK')
    ('HLA-C*01:02+HLA-C*01:03', {'HLA-C'}, 'OK')
    ('HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92', {'HLA-DRB5', 'HLA-DRB1'}, 'Phased - Check separately')

    Checking allele lists ...
    ('HLA-A*01:01/HLA-A*01:02', {'HLA-A'}, 'OK')
    ('HLA-B*44:01/HLA-B*44:02', {'HLA-B'}, 'OK')
    ('HLA-DRB1*04:07:01/HLA-DRB1*04:92', {'HLA-DRB1'}, 'OK')



example with a problem GL String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code ::

    $ ./checkgl.py -g 'HLA-A*01:01/HLA-B*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03^HLA-B*08:01+HLA-B*44:01/HLA-B*44:02^HLA-C*01:02+HLA-A*01:01~HLA-C*01:03^HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92'

    GL String = HLA-A*01:01/HLA-B*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03^HLA-B*08:01+HLA-B*44:01/HLA-B*44:02^HLA-C*01:02+HLA-A*01:01~HLA-C*01:03^HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92

    Checking locus blocks...
    HLA-A*01:01/HLA-B*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03
    HLA-B*08:01+HLA-B*44:01/HLA-B*44:02
    HLA-C*01:02+HLA-A*01:01~HLA-C*01:03
    HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92
    WARNING: Loci found in more than 1 locus block: {'HLA-B', 'HLA-A'}

    Checking genotype lists ...
    ('HLA-A*01:01/HLA-B*01:02+HLA-A*24:02|HLA-A*01:03+HLA-A*24:03', {'HLA-B', 'HLA-A'}, 'WARNING')

    Checking genotypes ...
    ('HLA-A*01:01/HLA-B*01:02+HLA-A*24:02', {'HLA-B', 'HLA-A'}, 'Unphased - WARNING')
    ('HLA-A*01:03+HLA-A*24:03', {'HLA-A'}, 'OK')
    ('HLA-B*08:01+HLA-B*44:01/HLA-B*44:02', {'HLA-B'}, 'OK')
    ('HLA-C*01:02+HLA-A*01:01~HLA-C*01:03', {'HLA-C', 'HLA-A'}, 'Phased - Check separately')
    ('HLA-DRB5*01:01~HLA-DRB1*03:01+HLA-DRB1*04:07:01/HLA-DRB1*04:92', {'HLA-DRB5', 'HLA-DRB1'}, 'Phased - Check separately')

    Checking allele lists ...
    ('HLA-A*01:01/HLA-B*01:02', {'HLA-B', 'HLA-A'}, 'WARNING')
    ('HLA-B*44:01/HLA-B*44:02', {'HLA-B'}, 'OK')
    ('HLA-DRB1*04:07:01/HLA-DRB1*04:92', {'HLA-DRB1'}, 'OK')


# doi2bib.py
Python script to generate BibTeX from DOI.

# Example
Input
```
./doi2bib.py 10.1137/s0036144504446096
```
Output
```
@article{gill2005snopt,
  doi = {10.1137/s0036144504446096},
  year = {2005},
  month = {jan},
  publisher = {Society for Industrial {\&} Applied Mathematics ({SIAM})},
  volume = {47},
  number = {1},
  pages = {99--131},
  author = {Philip E. Gill and Walter Murray and Michael A. Saunders},
  title = {{SNOPT}: An {SQP} Algorithm for Large-Scale Constrained Optimization},
  journal = {{SIAM} Review}
}
```

# Requirement
Python 3

# Usage
```
doi2bib.py [-h] [-i] [-x PROXY] ...

Generate BibTeX from DOI.

positional arguments:
  DOI

optional arguments:
  -h, --help            show this help message and exit
  -i                    run interactively
  -x PROXY, --proxy PROXY
                        set HTTP proxy
```

# License
This project is licensed under the terms of the MIT license.
